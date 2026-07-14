"""
Maybe refactor to apply to DRY ?
"""

from typing import Any, cast, List
from .json_states import State
from .functions_schema import FunctionSchema


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

    def _get_current_param_type(self) -> str:
        """Get function parameter's type"""
        if self.current_function and "parameters" in self.current_function:
            params = cast(dict[str, Any], self.current_function["parameters"])
            param_info = params.get(self.current_param_name, {})
            return param_info.get("type", "string")
        return "string"

    def get_expected_strings(self) -> List[str]:
        """Retourne les sous-chaînes exactes qu'on espère voir le LLM générer."""
        state = self.state

        if state == State.WAIT_FOR_OPEN_BRACE:
            return ["{"]

        elif state == State.EXPECT_PROMPT_KEY:
            return ['"prompt": "'.replace(self.text_buffer, "")]

        elif state == State.READING_PROMPT_VALUE:
            remainder = self.target_prompt.replace(self.text_buffer, "")
            return [remainder] if remainder else []

        elif state == State.EXPECT_NAME_KEY:
            return ['", "name": "'.replace(self.text_buffer, "")]

        elif state == State.READING_NAME_VALUE:
            encouraged = []
            for name in self.schema.get_all_names():
                if name.startswith(self.text_buffer):
                    remainder = name.replace(self.text_buffer, "", 1)
                    if remainder:
                        encouraged.append(remainder)
            return encouraged

        elif state == State.EXPECT_PARAMETERS_KEY:
            return ['", "parameters": {'.replace(self.text_buffer, "")]

        elif state == State.EXPECT_PARAM_KEY:
            if self.current_function and "parameters" in self.current_function:
                params = self.current_function["parameters"]
                param_keys = [
                    k for k in params.keys() if k not in self.generated_params
                ]

                encouraged = []
                for k in param_keys:
                    expected_str = f'"{k}": '
                    if expected_str.startswith(self.text_buffer):
                        remainder = expected_str.replace(self.text_buffer, "", 1)
                        if remainder:
                            encouraged.append(remainder)
                return encouraged
            return []

        elif state == State.READING_PARAM_VALUE:
            if self._get_current_param_type() == "string" and self.text_buffer == "":
                return ['"']
            return []

        elif state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
            encouraged = []
            if self.current_function and "parameters" in self.current_function:
                params = self.current_function["parameters"]
                remaining = [k for k in params.keys() if k not in self.generated_params]
                if remaining:
                    encouraged.append(", ")
            encouraged.append("}")
            return encouraged

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

        if self.state == State.WAIT_FOR_OPEN_BRACE:
            self._static_transition("{", State.EXPECT_PROMPT_KEY)

        elif self.state == State.EXPECT_PROMPT_KEY:
            self._static_transition('"prompt": "', State.READING_PROMPT_VALUE)

        elif self.state == State.READING_PROMPT_VALUE:
            self._static_transition(self.target_prompt, State.EXPECT_NAME_KEY)

        elif self.state == State.EXPECT_NAME_KEY:
            self._static_transition('", "name": "', State.READING_NAME_VALUE)

        elif self.state == State.READING_NAME_VALUE:
            if self.text_buffer in self.schema.get_all_names():
                self.current_function = self.schema.get_function(self.text_buffer)
                self.generated_params.clear()
                self.state = State.EXPECT_PARAMETERS_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_PARAMETERS_KEY:
            self._static_transition('", "parameters": {', State.EXPECT_PARAM_KEY)

        elif self.state == State.EXPECT_PARAM_KEY:
            if self.current_function and "parameters" in self.current_function:
                for k in self.current_function["parameters"].keys():
                    expected_str = f'"{k}": '
                    if expected_str in self.text_buffer:
                        self.current_param_name = k
                        self.generated_params.add(k)
                        self.state = State.READING_PARAM_VALUE
                        self.text_buffer = ""
                        break

        elif self.state == State.READING_PARAM_VALUE:
            param_type = self._get_current_param_type()
            if param_type == "string":
                if (
                    self.text_buffer.startswith('"')
                    and self.text_buffer.endswith('"')
                    and len(self.text_buffer) > 1
                    and not self.text_buffer.endswith('\\"')
                ):
                    self.state = State.EXPECT_PARAM_COMMA_OR_CLOSE
                    self.text_buffer = ""
            elif param_type in ["number", "integer"]:
                if "," in self.text_buffer:
                    self.state = State.EXPECT_PARAM_KEY
                    self.text_buffer = ""
                elif "}" in self.text_buffer:
                    self.state = State.EXPECT_CLOSE_BRACE
                    self.text_buffer = ""

        elif self.state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
            if ", " in self.text_buffer:
                self.state = State.EXPECT_PARAM_KEY
                self.text_buffer = ""
            elif "}" in self.text_buffer:
                self.state = State.EXPECT_CLOSE_BRACE
                self.text_buffer = ""
