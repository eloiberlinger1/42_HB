from llm_sdk import (
    Small_LLM_Model,
)  # comment eviter de devoir repeter ca juste pour le typehint ?
from .json_format_constraint import JSONFormatConstraint


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

        prompt_ids = model._tokenizer.encode(prompt, add_special_tokens=False)
        generated_ids = list(prompt_ids)

        # vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json
        # vocab_path = model.get_path_to_vocab_file()

        max_new_tokens = 20  # for dev
        constraint = self.constraint_engine

        result = ""

        for i in range(max_new_tokens):
            print(f"Iteration {i}/{max_new_tokens}")
            print(f"result value: {result}")

            next_token_logits = model.get_logits_from_input_ids(generated_ids)

            next_token_id = constraint.apply_constraint(
                next_token_logits, result
            )

            generated_ids.append(next_token_id)
            result += model._tokenizer.decode([next_token_id])

            if next_token_id == model._tokenizer.eos_token_id:
                break

        return result
