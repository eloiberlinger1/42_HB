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


class JSONState(Enum):
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

    def __init__(self, model_vocab_path, functions_file_path):
        self.state = JSONState.WAIT_FOR_OPEN_BRACE
        self.current_function_info = None

        with open(model_vocab_path, "r", encoding="utf-8") as f:
            self.vocab = json.load(f)
        with open(functions_file_path, "r", encoding="utf-8") as f:
            self.defined_functions = json.load(f)

        self.functions = {f["name"]: f for f in self.defined_functions}
        print(f"Loaded functions : {self.functions}")

    def _check_state(self, current_text: str) -> str:
        """
        Handles the already generated text to make sure the generation follows the defined rules.
        """
        if not current_text:
            return "WAIT_FOR_OPEN_BRACE"

        if current_text == "{":
            return "EXPECT_PROMPT_KEY"
        if current_text.endswith('{"prompt": "'):
            return "READING_PROMPT_VALUE"

        # TODO: Ajouter les autres transitions avec des expressions régulières (Regex)
        # Par exemple, détecter si on vient de finir d'écrire le nom de la fonction
        # pour charger ses paramètres spécifiques.

        return "FREE_TEXT"

    def get_encouraged_ids(self) -> list[int]:
        """
        Returns a list of the ids to expect accordint to the
        already written json.
        """

        state = self.state

        if state == JSONState.WAIT_FOR_OPEN_BRACE:
            return [self.vocab.get("{")]

        elif state == JSONState.EXPECT_PROMPT_KEY:
            return [self.vocab.get.get('"prompt": "')]

        elif state == JSONState.READING_NAME_VALUE:
            return [self.vocab.get(name) for name in self.functions.keys()]

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
