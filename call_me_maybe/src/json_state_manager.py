from typing import Any, List, cast

from .functions_schema import FunctionSchema
from .json_states import State


class JSONStateManager:
    """
    Encourage the llm to take decisions that
    follows the JSON expected output format.

    Example of excepted output format:

    {
        "prompt": "prompt from function_calling_tests.json",
        "name": "fn_functionname",
        "parameters": {"a": 2.0, "b": 3.0}
    }
    """

    def __init__(self, target_prompt: str, schema: FunctionSchema):
        self.state = State.WAIT_FOR_OPEN_BRACE
        self.target_prompt = target_prompt
        self.schema = schema

        self.text_buffer = ""
        self.current_function: dict[str, Any] | None = None
        self.current_param_name = ""
        self.generated_params: set[str] = set()
        self.is_done: bool = False

    def _get_current_param_type(self) -> str:
        """Get function parameter's type"""
        if self.current_function and "parameters" in self.current_function:
            params = cast(dict[str, Any], self.current_function["parameters"])
            param_info = params.get(self.current_param_name, {})
            return param_info.get("type", "string")
        return "string"

    def _has_missing_parameters(self) -> bool:
        if (
            not self.current_function
            or "parameters" not in self.current_function
        ):
            return False
        expected_params = set(self.current_function["parameters"].keys())
        return len(expected_params - self.generated_params) > 0

    def get_expected_strings(self) -> List[str]:
        state = self.state
        buf = self.text_buffer

        if state == State.WAIT_FOR_OPEN_BRACE:
            if "{".startswith(buf):
                return ["{"[len(buf):]]

        elif state == State.EXPECT_PROMPT_KEY:
            expected = '"prompt": "'
            if expected.startswith(buf):
                return [expected[len(buf):]]

        elif state == State.READING_PROMPT_VALUE:
            expected = self.target_prompt
            if expected.startswith(buf):
                return [expected[len(buf):]]

        elif state == State.EXPECT_NAME_KEY:
            expected = '", "name": "'
            if expected.startswith(buf):
                return [expected[len(buf):]]

        elif state == State.READING_NAME_VALUE:
            encouraged = []
            for name in self.schema.get_all_names():
                if name.startswith(buf):
                    rem = name[len(buf):]
                    if rem:
                        encouraged.append(rem)
            return encouraged

        elif state == State.EXPECT_PARAMETERS_KEY:
            expected = '", "parameters": {'
            if expected.startswith(buf):
                return [expected[len(buf):]]

        elif state == State.EXPECT_PARAM_KEY:
            buf_stripped = buf.lstrip()
            if self.current_function and "parameters" in self.current_function:
                params = self.current_function["parameters"]
                param_keys = [
                    k for k in params.keys() if k not in self.generated_params
                ]

                encouraged = []
                for k in param_keys:
                    expected_str = f'"{k}": '
                    if expected_str.startswith(buf_stripped):
                        rem = expected_str[len(buf_stripped):]
                        if rem:
                            encouraged.append(rem)
                return encouraged

        elif state == State.READING_PARAM_VALUE:
            if self._get_current_param_type() == "string" and buf == "":
                return ['"']

        elif state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
            expected = ", " if self._has_missing_parameters() else "}"
            buf_stripped = buf.lstrip()
            if expected.startswith(buf_stripped):
                rem = expected[len(buf_stripped):]
                if rem:
                    return [rem]
            return [expected]

        elif state == State.EXPECT_CLOSE_BRACE:
            expected = "}"
            buf_stripped = buf.lstrip()
            if expected.startswith(buf_stripped):
                rem = expected[len(buf_stripped):]
                if rem:
                    return [rem]
            return ["}"]

        return []

    #
    #
    #
    #

    def _static_transition(self, expected_string: str, new_state: State):
        if expected_string in self.text_buffer:
            self.state = new_state
            self.text_buffer = self.text_buffer.split(expected_string, 1)[1]

    def transition(self, token_text: str) -> None:
        """Step the state ahead according to the decoded token"""
        if not token_text:
            return

        self.text_buffer += token_text

        while True:
            initial_state = self.state

            if self.state == State.WAIT_FOR_OPEN_BRACE:
                self._static_transition("{", State.EXPECT_PROMPT_KEY)

            elif self.state == State.EXPECT_PROMPT_KEY:
                self._static_transition(
                    '"prompt": "',
                    State.READING_PROMPT_VALUE
                )

            elif self.state == State.READING_PROMPT_VALUE:
                self._static_transition(
                    self.target_prompt,
                    State.EXPECT_NAME_KEY
                )

            elif self.state == State.EXPECT_NAME_KEY:
                self._static_transition(
                    '", "name": "',
                    State.READING_NAME_VALUE
                )

            elif self.state == State.READING_NAME_VALUE:
                for name in self.schema.get_all_names():
                    if name in self.text_buffer:
                        self.current_function = self.schema.get_function(name)
                        self.generated_params.clear()
                        self.state = State.EXPECT_PARAMETERS_KEY
                        self.text_buffer = self.text_buffer.split(name, 1)[1]
                        break

            elif self.state == State.EXPECT_PARAMETERS_KEY:
                self._static_transition(
                    '", "parameters": {',
                    State.EXPECT_PARAM_KEY
                )

            elif self.state == State.EXPECT_PARAM_KEY:
                if "}" in self.text_buffer:
                    if not self._has_missing_parameters():
                        self._static_transition("}", State.EXPECT_CLOSE_BRACE)
                    else:
                        self.text_buffer = self.text_buffer.replace("}", "")

                if (
                    self.current_function
                    and "parameters" in self.current_function
                ):
                    for k in self.current_function["parameters"].keys():
                        expected_str = f'"{k}": '
                        if expected_str in self.text_buffer:
                            self.current_param_name = k
                            self.generated_params.add(k)
                            self.state = State.READING_PARAM_VALUE
                            self.text_buffer = self.text_buffer.split(
                                expected_str,
                                1
                            )[1]
                            break

            elif self.state == State.READING_PARAM_VALUE:
                param_type = self._get_current_param_type()
                if param_type == "string":
                    if '"' in self.text_buffer:
                        start_idx = self.text_buffer.find('"')
                        escaped = False
                        end_idx = -1
                        for i in range(start_idx + 1, len(self.text_buffer)):
                            if self.text_buffer[i] == "\\" and not escaped:
                                escaped = True
                            elif self.text_buffer[i] == '"' and not escaped:
                                end_idx = i
                                break
                            else:
                                escaped = False

                        if end_idx != -1:
                            self.state = State.EXPECT_PARAM_COMMA_OR_CLOSE
                            self.text_buffer = self.text_buffer[end_idx + 1:]

                elif param_type in ["number", "integer"]:
                    if "," in self.text_buffer:
                        self.state = State.EXPECT_PARAM_KEY
                        self.text_buffer = self.text_buffer.split(",", 1)[1]
                    elif "}" in self.text_buffer:
                        if not self._has_missing_parameters():
                            self.state = State.EXPECT_CLOSE_BRACE
                            self.text_buffer = self.text_buffer.split(
                                "}",
                                1)[1]
                        else:
                            self.text_buffer = self.text_buffer.replace(
                                "}", "")

            elif self.state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
                if "," in self.text_buffer:
                    self.state = State.EXPECT_PARAM_KEY
                    self.text_buffer = self.text_buffer.split(",", 1)[1]
                elif "}" in self.text_buffer:
                    if not self._has_missing_parameters():
                        self.state = State.EXPECT_CLOSE_BRACE
                        self.text_buffer = self.text_buffer.split("}", 1)[1]
                    else:
                        self.text_buffer = self.text_buffer.replace("}", "")

            elif self.state == State.EXPECT_CLOSE_BRACE:
                if "}" in self.text_buffer:
                    self.state = State.DONE
                    self.text_buffer = self.text_buffer.split("}", 1)[1]

            if self.state == initial_state:
                break
