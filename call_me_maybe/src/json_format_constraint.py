"""
Follow the generated tokens to guide the llm so it will choose JSON format characters when needed

Example of excepted format:

{
  "prompt": "prompt from function_calling_tests.json",
  "name": "fn_functionname",
  "parameters": {"a": 2.0, "b": 3.0}
}

"""

from enum import Enum, auto
import numpy as np
import json


class State(Enum):
    WAIT_FOR_OPEN_BRACE = auto()
    EXPECT_PROMPT_KEY = auto()
    READING_PROMPT_VALUE = auto()

    EXPECT_NAME_KEY = auto()
    READING_NAME_VALUE = auto()

    EXPECT_PARAMETERS_KEY = auto()
    EXPECT_PARAM_OPEN_BRACE = auto()

    EXPECT_PARAM_KEY = auto()
    EXPECT_PARAM_COLON = auto()
    READING_PARAM_VALUE = auto()
    EXPECT_PARAM_COMMA_OR_CLOSE = auto()

    EXPECT_CLOSE_BRACE = auto()
    DONE = auto()


class JSONFormatConstraint:

    def __init__(self, model, functions_file_path, prompt: str):
        self.state = State.WAIT_FOR_OPEN_BRACE
        self.current_function_info = None
        self.target_prompt = prompt

        self.model = model
        model_vocab_path = model.get_path_to_vocab_file()

        with open(model_vocab_path, "r", encoding="utf-8") as f:
            self.vocab = json.load(f)
        with open(functions_file_path, "r", encoding="utf-8") as f:
            self.defined_functions = json.load(f)

        self.functions = {f["name"]: f for f in self.defined_functions}

    def _check_state(self, current_text: str) -> State:
        """
        Handles the already generated text to make sure the generation follows
        the defined rules.
        """
        if not current_text:
            self.state = State.WAIT_FOR_OPEN_BRACE
            return self.state

        if self.state == State.WAIT_FOR_OPEN_BRACE and current_text == "{":
            self.state = State.EXPECT_PROMPT_KEY

        elif self.state == State.EXPECT_PROMPT_KEY and current_text.endswith(
            '{"prompt": "'
        ):
            self.state = State.READING_PROMPT_VALUE

        elif (
            self.state == State.READING_PROMPT_VALUE
            and current_text.endswith('", "name": "')
        ):
            self.state = State.READING_NAME_VALUE

        elif self.state == State.READING_NAME_VALUE:
            if current_text.endswith('", "parameters": {'):
                self.state = State.EXPECT_PARAM_KEY

                partie_name = current_text.split('"name": "')[-1]
                nom_fonction = partie_name.split('", "parameters"')[0]

                self.current_function = self.functions.get(nom_fonction)
                self.param_keys_to_generate = (
                    list(self.current_function["parameters"].keys())
                    if self.current_function
                    else []
                )

        return self.state

    def get_encouraged_ids(self) -> list[int]:
        """
        Returns a list of the ids to expect accordint to the
        already written json.
        """

        state = self.state
        tokenizer = self.model.tokenizer

        if state == State.WAIT_FOR_OPEN_BRACE:
            return tokenizer.encode("{", add_special_tokens=False)

        elif state == State.EXPECT_PROMPT_KEY:
            tokens = tokenizer.encode('"prompt": "', add_special_tokens=False)
            return [tokens[0]] if tokens else []

        elif state == State.READING_PROMPT_VALUE:
            tokens = tokenizer.encode(
                self.target_prompt, add_special_tokens=False
            )
            return [tokens[0]] if tokens else []

        elif state == State.EXPECT_NAME_KEY:
            tokens = tokenizer.encode('", "name": "', add_special_tokens=False)
            return [tokens[0]] if tokens else []

        elif state == State.READING_NAME_VALUE:
            encouraged = []
            for name in self.functions.keys():
                tokens = tokenizer.encode(name, add_special_tokens=False)
                if tokens:
                    encouraged.append(tokens[0])
            return list(set(encouraged))

        return []

    def apply_constraint(self, token_logits: list[float], result: str):
        print(f"Current state : {self.state}")

        encouraged_ids = self.get_encouraged_ids()
        print(f"Current state : {self.state}")

        next_token_logits = np.array(token_logits)

        mask = np.full_like(next_token_logits, -float("inf"))

        for i in encouraged_ids:
            if i == -1:
                break
            mask[i] = next_token_logits[i]
        next_token_logits = mask

        next_token_id = int(np.argmax(next_token_logits))

        return next_token_id
