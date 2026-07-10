from llm_sdk import Small_LLM_Model
import math
import json


class ConstrainedDecoder:
    """
    Handles the token generation loop

    """

    def __init__(self):

        self.model = Small_LLM_Model()

    def decode(self):

        model = self.model
        max_new_tokens = 20
        generated_ids = list(input_ids)

        # vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json
        vocab_path = model.get_path_to_vocab_file()
        with open(vocab_path, "r", encoding="utf-8") as f:
            vocab_dict = json.load(f)

        for i in range(max_new_tokens):
            logits = model.get_logits_from_input_ids(generated_ids)

            #     90 =  "{"
            # cette variable doit changer en fonction de la generation et des etapes du controlleur d'etat JSON
            tokens_autorises = [90]

            constrained_logits = []

            for token_id, logit_value in enumerate(logits):
                if token_id in tokens_autorises:
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

        print(final_text)
