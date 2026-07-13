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
    """
    Applies the constraints on each iteration of the token generation to
    control the output and encourage the llm to take decisions that 
    follows the JSON expected output format.
    """

    def __init__(self, model, functions_file_path, prompt: str):
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
        self.current_function = ""

    def get_encouraged_ids(self) -> list[int]:
        """
        Returns a list of the ids to expect accordint to the
        already written json.

        This function looks no the buffer what still have to be written
        before it can go to the next JSONState.
        """

        state = self.state
        tokenizer = self.model._tokenizer

        if state == State.WAIT_FOR_OPEN_BRACE:
            return tokenizer.encode("{", add_special_tokens=False)

        elif state == State.EXPECT_PROMPT_KEY:
            remainder = '"prompt": "'.replace(self.text_buffer, "")
            tokens = tokenizer.encode(remainder, add_special_tokens=False)
            return [tokens[0]] if tokens else []

        elif state == State.READING_PROMPT_VALUE:
            full_expected = self.target_prompt
            remainder = full_expected.replace(self.text_buffer, "")
            tokens = tokenizer.encode(remainder, add_special_tokens=False)
            return [tokens[0]] if tokens else []
        
        elif state == State.EXPECT_NAME_KEY:
            full_expected = '", "name": "'
            remainder = full_expected.replace(self.text_buffer, "")
            tokens = tokenizer.encode(remainder, add_special_tokens=False)
            return [tokens[0]] if tokens else []
        
        elif state == State.READING_NAME_VALUE:
            encouraged = []
            for f in self.functions.keys():
                if f.startswith(self.text_buffer):
                    remainder = f.replace(self.text_buffer, "", 1)
                    if remainder != "":
                        tokens = tokenizer.encode(remainder, add_special_tokens=False)
                        if tokens:
                            encouraged.append(tokens[0])
            
            return list(set(encouraged))

        elif state == State.EXPECT_PARAMETERS_KEY:
            # TODO : maybe associate each expected remainder directly in the state value ?
            remainder = '", "parameters": {'.replace(self.text_buffer, "")
            tokens = tokenizer.encode(remainder, add_special_tokens=False)
            return [tokens[0]] if tokens else []
        
        elif state == State.EXPECT_PARAM_COLON:
            remainder = '"'.replace(self.text_buffer, "")
            tokens = tokenizer.encode(remainder, add_special_tokens=False)
            return [tokens[0]] if tokens else []

        elif state == State.EXPECT_PARAM_KEY:
                
                print()
                print()
            
                print(f"self.current_function = {self.current_function}")
                print()
                expected_keys = self.current_function["parameters"].keys()
                print(f"expected_keys : {expected_keys}")
                # the key should match the paramaters for the functions def

                remainder = '"'.replace(self.text_buffer, "")
                tokens = tokenizer.encode(remainder, add_special_tokens=False)
                return [tokens[0]] if tokens else []

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
                self.state = State.EXPECT_PARAM_COLON
                self.text_buffer = ""
        
        elif self.state == State.EXPECT_PARAM_COLON:
            if '"' in self.text_buffer:
                self.state = State.EXPECT_PARAM_KEY
                self.text_buffer = ""

        elif self.state == State.EXPECT_PARAM_KEY:
            if 'paramaeterkey' in self.text_buffer:
                self.state = State.next
                self.text_buffer = ""        


    def apply_constraint(self, token_logits: list[float]):
        """
        In order to just pick the token with the highest score (max())
        Here we manually change the probabilities to encourage the expected caracters
        according to the JSON state.
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
        print(f"Token choisi : '{last_token_text}' | Transition depuis l'état : {self.state}")
        
        self.state_transition(last_token_text)

        print(f"Nouvel etat: {self.state}")        

        return next_token_id

