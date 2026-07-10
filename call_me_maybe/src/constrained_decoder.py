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
        self.model = Small_LLM_Model()
        self.constraint_engine = constraint_engine

    def generate(self, prompt: str, max_new_tokens: int = 150) -> str:
        """
        Generate constrained tokens
        """
        model = self.model
        input_ids = self.model.encode(prompt)
        generated_ids = list(input_ids)

        # vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json
        # vocab_path = model.get_path_to_vocab_file()

        for i in range(max_new_tokens):
            logits = model.get_logits_from_input_ids(generated_ids)

            input_ids_len = len(input_ids)
            tokens_generes = generated_ids[input_ids_len:]
            actual_text = (
                self.model.decode(tokens_generes) if tokens_generes else ""
            )

            #     90 =  "{"
            # cette variable doit changer en fonction de la generation et des etapes du controlleur d'etat JSON
            encouraged_token = [90]

            constrained_logits = self.constraint_engine.get_allowed_tokens(
                generated_ids
            )

            for token_id, logit_value in enumerate(logits):
                if token_id in encouraged_token:
                    constrained_logits.append(logit_value)
                else:
                    constrained_logits.append(-math.inf)

            next_token_id = max(
                range(len(constrained_logits)),
                key=lambda i: constrained_logits[i],
            )

            if next_token_id == model._tokenizer.eos_token_id:
                break

            generated_ids.append(next_token_id)

        final_text = model.decode(generated_ids)

        print("affichage de la reponse")

        return final_text
