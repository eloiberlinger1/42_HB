from __future__ import annotations

from typing import TYPE_CHECKING

from .json_logits_processor import JSONLogitsProcessor
from .logger import log

if TYPE_CHECKING:
    from llm_sdk import Small_LLM_Model


class ConstrainedDecoder:
    """
    Handles the token generation loop

    """

    def __init__(
        self,
        model: Small_LLM_Model,
        logits_processor: JSONLogitsProcessor
    ):
        self.model = model
        self.logits_processor = logits_processor

    def generate(self, prompt: str, max_new_tokens: int = 150) -> str:
        """
        Generate constrained tokens
        """

        model = self.model

        prompt_tensor = model.encode(prompt)
        generated_ids = prompt_tensor.squeeze(0).tolist()

        constraint = self.logits_processor

        result = ""

        for i in range(max_new_tokens):
            log(f"Iteration {i}/{max_new_tokens}")
            log(f"result value: {result}")

            next_token_logits = model.get_logits_from_input_ids(generated_ids)
            next_token_id = constraint.apply_constraint(next_token_logits)

            generated_ids.append(next_token_id)

            result += model.decode([next_token_id])

            # -> Direct access to model._tokenizer.eos_token_id
            if next_token_id == model._tokenizer.eos_token_id:
                break

        return result
