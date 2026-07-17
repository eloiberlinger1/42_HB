"""
Follow the generated tokens to guide the llm so it
will choose JSON format characters when needed
"""

from typing import cast

import numpy as np

from llm_sdk import Small_LLM_Model

from .json_state_manager import JSONStateManager
from .json_states import State
from .logger import log


class JSONLogitsProcessor:
    """
    Applies the constraints on each iteration of the token generation to
    control the output and
    """

    def __init__(
        self,
        model: Small_LLM_Model,
        state_manager: JSONStateManager
    ):
        self.model = model
        self.state_manager = state_manager

    def _encode_first_token(self, text: str) -> int | None:
        """-- Encode a string and returns only it's first token"""
        tensor_2d = self.model.encode(text)
        tokens = cast(list[int], tensor_2d.squeeze(0).tolist())
        return tokens[0] if tokens else None

    def apply_constraint(self, token_logits: list[float]) -> int:
        """
        Apply the constraint on the logits
        to force LLM to follow the expected output
        """
        if self.state_manager.state == State.DONE:
            return int(self.model._tokenizer.eos_token_id)
        expected_strings = self.state_manager.get_expected_strings()

        encouraged_ids = []
        for text in expected_strings:
            token_id = self._encode_first_token(text)
            if token_id is not None:
                encouraged_ids.append(token_id)

        encouraged_ids = list(set(encouraged_ids))
        next_token_logits = np.array(token_logits)

        if not encouraged_ids:
            if self.state_manager._has_missing_parameters():
                while True:
                    best_token_id = int(np.argmax(next_token_logits))
                    best_token_text = self.model.decode(
                        [best_token_id]
                    )

                    if "}" in best_token_text:
                        next_token_logits[best_token_id] = -float("inf")
                    else:
                        next_token_id = best_token_id
                        break

            next_token_id = int(np.argmax(next_token_logits))

        else:
            mask = np.full_like(next_token_logits, -float("inf"))

            for i in encouraged_ids:
                mask[i] = next_token_logits[i]
            next_token_id = int(np.argmax(mask))

        last_token_text = self.model.decode([next_token_id])

        log(
            f"Choosed token : '{last_token_text}'"
            + " | Transition from state : {self.state_manager.state}"
        )
        self.state_manager.transition(str(last_token_text))
        log(f"New state : {self.state_manager.state}")

        return next_token_id
