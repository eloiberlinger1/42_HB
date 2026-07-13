"""
Follow the generated tokens to guide the llm so it
will choose JSON format characters when needed

Example of excepted format:

{
  "prompt": "prompt from function_calling_tests.json",
  "name": "fn_functionname",
  "parameters": {"a": 2.0, "b": 3.0}
}

"""

from llm_sdk import Small_LLM_Model  # Just for type hint
from typing import Any, cast
import torch

from .json_states import State
import numpy as np
import json


class JSONFormatConstraint:
    """
    Applies the constraints on each iteration of the token generation to
    control the output and encourage the llm to take decisions that
    follows the JSON expected output format.
    """

    def __init__(self, model: Small_LLM_Model, functions_file_path: str, prompt: str):
        self.state = State.WAIT_FOR_OPEN_BRACE
        self.target_prompt = prompt

        self.model = model
        model_vocab_path = model.get_path_to_vocab_file()

        with open(model_vocab_path, "r", encoding="utf-8") as f:
            self.vocab = json.load(f)
        with open(functions_file_path, "r", encoding="utf-8") as f:
            self.defined_functions = json.load(f)

        self.functions = {f["name"]: f for f in self.defined_functions}
        self.text_buffer = ""
        self.current_function: dict[str, Any] | None = None

    def _encode_to_list(self, text: str) -> list[int]:
        """
        Encode text and make sure to get a 2D list
        """
        tensor_2d: torch.Tensor = self.model.encode(text)

        return cast(list[int], tensor_2d.squeeze(0).tolist())

    def _get_current_param_type(self) -> str:
        """Get function parameter's type"""
        if self.current_function and "parameters" in self.current_function:
            params = cast(dict[str, Any], self.current_function["parameters"])
            param_info = params.get(self.current_param_name, {})
            return param_info.get("type", "string")
        return "string"

    def get_encouraged_ids(self) -> list[int]:
        """
        Returns a list of the ids to expect accordint to the
        already written json.

        This function looks no the buffer what still have to be written
        before it can go to the next JSONState.
        """

        state = self.state

        if state == State.WAIT_FOR_OPEN_BRACE:
            return self._encode_to_list("{")

        elif state == State.EXPECT_PROMPT_KEY:
            remainder = '"prompt": "'.replace(self.text_buffer, "")
            return self._encode_to_list(remainder)

        elif state == State.READING_PROMPT_VALUE:
            full_expected = self.target_prompt
            remainder = full_expected.replace(self.text_buffer, "")
            return self._encode_to_list(remainder)

        elif state == State.EXPECT_NAME_KEY:
            full_expected = '", "name": "'
            remainder = full_expected.replace(self.text_buffer, "")
            return self._encode_to_list(remainder)

        elif state == State.READING_NAME_VALUE:
            encouraged = []
            for f in self.functions.keys():
                if f.startswith(self.text_buffer):
                    remainder = f.replace(self.text_buffer, "", 1)
                    if remainder != "":
                        tokens = self._encode_to_list(remainder)
                        if tokens:
                            encouraged.append(tokens[0])

            return list(set(encouraged))

        elif state == State.EXPECT_PARAMETERS_KEY:
            remainder = '", "parameters": {'.replace(self.text_buffer, "")
            tokens = self._encode_to_list(remainder)
            return [tokens[0]] if tokens else []

        elif state == State.EXPECT_PARAM_KEY:
            if (
                self.current_function is not None
                and "parameters" in self.current_function
            ):
                params = cast(dict[str, Any], self.current_function["parameters"])
                param_keys = params.keys()

                encouraged = []
                for k in param_keys:
                    expected_str = f'"{k}": '
                    if expected_str.startswith(self.text_buffer):
                        remainder = expected_str.replace(self.text_buffer, "", 1)
                        if remainder:
                            tokens = self._encode_to_list(remainder)
                            if tokens:
                                encouraged.append(tokens[0])
                return list(set(encouraged))

        elif state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
            # On encourage soit la virgule (pour un autre paramètre)
            # soit l'accolade fermante     ex: ", " ou "}"

            # TODO : count the number of parameters
            encouraged = []
            tokens_comma = self._encode_to_list(", ")
            tokens_close = self._encode_to_list("}")
            if tokens_comma:
                encouraged.append(tokens_comma[0])
            if tokens_close:
                encouraged.append(tokens_close[0])
            return encouraged

            return list(set(encouraged))

        elif state == State.READING_PARAM_VALUE:
            param_type = self._get_current_param_type()

            if param_type == "string":
                if self.text_buffer == "":
                    return self._encode_to_list('"')

        return []

    def state_transition(self, token_text: str) -> None:

        if not token_text:
            return

        self.text_buffer += token_text

        if self.state == State.WAIT_FOR_OPEN_BRACE:
            if "{" in self.text_buffer:
                self.state = State.EXPECT_PROMPT_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_PROMPT_KEY:
            if '"prompt": "' in self.text_buffer:
                self.state = State.READING_PROMPT_VALUE
                self.text_buffer = ""

        elif self.state == State.READING_PROMPT_VALUE:
            if self.target_prompt in self.text_buffer:
                self.state = State.EXPECT_NAME_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_NAME_KEY:
            if '", "name": "' in self.text_buffer:
                self.state = State.READING_NAME_VALUE
                self.text_buffer = ""

        elif self.state == State.READING_NAME_VALUE:
            if self.text_buffer in self.functions:
                self.current_function = self.functions[self.text_buffer]
                self.state = State.EXPECT_PARAMETERS_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_PARAMETERS_KEY:
            if '", "parameters": {' in self.text_buffer:
                self.state = State.EXPECT_PARAM_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_PARAM_KEY:
            curr_fn = self.current_function
            if curr_fn is not None and "parameters" in curr_fn:
                params = cast(dict[str, Any], curr_fn["parameters"])
                for k in params.keys():
                    expected_str = f'"{k}": '
                    if expected_str in self.text_buffer:
                        self.current_param_name = k
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
                ):
                    self._transition_after_param_value()

            elif param_type in ["number", "integer"]:
                if "," in self.text_buffer or "}" in self.text_buffer:
                    self._transition_after_param_value()

        elif self.state == State.EXPECT_PARAM_COMMA_OR_CLOSE:
            if ", " in self.text_buffer:
                self.state = State.EXPECT_PARAM_KEY
                self.text_buffer = ""
            elif "}" in self.text_buffer:
                self.state = State.EXPECT_CLOSE_BRACE
                self.text_buffer = ""

    def _transition_after_param_value(self):
        """Détermine si on attend un autre paramètre ou la fin du JSON."""
        if "}" in self.text_buffer:
            self.state = State.EXPECT_CLOSE_BRACE
        elif "," in self.text_buffer:
            self.state = State.EXPECT_PARAM_KEY
        else:
            self.state = State.EXPECT_PARAM_COMMA_OR_CLOSE

        self.text_buffer = ""

    def apply_constraint(self, token_logits: list[float]):
        """
        In order to just pick the token with the highest score (max())
        Here we manually change the probabilities to encourage
        the expected caracters according to the JSON state.
        """

        encouraged_ids = self.get_encouraged_ids()

        next_token_logits = np.array(token_logits)
        mask = np.full_like(next_token_logits, -float("inf"))

        if not encouraged_ids:
            next_token_id = int(np.argmax(next_token_logits))
        else:
            for i in encouraged_ids:
                mask[i] = next_token_logits[i]
            next_token_id = int(np.argmax(mask))

        last_token_text = self.model._tokenizer.decode([next_token_id])
        print(
            f"Token choisi : '{last_token_text}' | "
            f"Transition depuis l'état : {self.state}"
        )

        self.state_transition(last_token_text)

        print(f"Nouvel etat: {self.state}")

        return next_token_id
