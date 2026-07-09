import math
import os
import sys

from llm_sdk import Small_LLM_Model

model = Small_LLM_Model()
# vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json

prompt = (
        "Select the correct function name to satisfy the user request.\n\n"
        "Available functions:\n"
        "- fn_add_numbers: Add two numbers together and return their sum.\n"
        "- fn_greet: Generate a greeting message for a person by name.\n\n"
        "User Request: \"What is the sum of 40 and 2?\"\n\n"
        "The correct function to use is: fn_"
    )
input_ids = model._tokenizer.encode(prompt, add_special_tokens=False)

max_new_tokens = 100
generated_ids = list(input_ids)

for i in range(max_new_tokens):
    print(f"iteration : {i}")
    logits = model.get_logits_from_input_ids(generated_ids)

    print(f"logit {i}: {logits[i]}")

    # c. Appliquer les contraintes (Constrained Decoding)
    # On force à -infini tous les tokens qui violeraient la syntaxe ou le schéma JSON
    constrained_logits = []
    for token_id, logit_value in enumerate(logits):
        constrained_logits.append(logit_value)

    # d. Sélectionner le token (Argmax parmi les tokens autorisés)
    next_token_id = max(
        range(len(constrained_logits)), key=lambda i: constrained_logits[i]
    )

    if next_token_id == model._tokenizer.eos_token_id:
        break

    generated_ids.append(next_token_id)

print(generated_ids)

final_text = model.decode(generated_ids)

print("affichage de la reponse")

print(final_text)
