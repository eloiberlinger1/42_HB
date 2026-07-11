from typing import List
from llm_sdk import (
    Small_LLM_Model,
)  # comment eviter de devoir repeter ca juste pour le typehint ?
from .json_format_constraint import JSONFormatConstraint

import math
import json


class ConstrainedDecoder:
    """
    Handles the token generation loop

    """

    def __init__(
        self, model: Small_LLM_Model, constraint_engine: JSONFormatConstraint
    ):
        self.model = model
        self.constraint_engine = constraint_engine

    def generate(self, prompt: str, max_new_tokens: int = 150) -> str:
        """
        Generate constrained tokens
        """
        model = self.model

        input_ids = model._tokenizer.encode(prompt, add_special_tokens=False)
        generated_ids = list(input_ids)

        print("Input ids :")
        print(input_ids)
        
        # vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json
        # vocab_path = model.get_path_to_vocab_file()

        for i in range(max_new_tokens):
            all_logits = model.get_logits_from_input_ids(list(input_ids))
            
            print(all_logits)

