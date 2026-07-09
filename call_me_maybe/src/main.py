import sys
import os
import math
from llm_sdk import Small_LLM_Model

model = Small_LLM_Model()

prompt = "Who are you ?"
input_ids = model._tokenizer.encode(prompt, add_special_tokens=False)

max_new_tokens = 150
generated_ids = list(input_ids)

for _ in range(max_new_tokens):
    logits = model.get_logits_from_input_ids(generated_ids)

    # b. Identifier les tokens valides à cette étape (votre logique de parsing / automate)
    # Exemple : si on attend le nom de la fonction, seuls les caractères de "fn_add_numbers" sont valides
    valid_token_ids = [
        42,
        103,
        502,
    ]  # À déterminer dynamiquement selon l'état de votre JSON

    # c. Appliquer les contraintes (Constrained Decoding)
    # On force à -infini tous les tokens qui violeraient la syntaxe ou le schéma JSON
    constrained_logits = []
    for token_id, logit_value in enumerate(logits):
        if token_id in valid_token_ids:
            constrained_logits.append(logit_value)
        else:
            constrained_logits.append(-math.inf)

    # d. Sélectionner le token (Argmax parmi les tokens autorisés)
    next_token_id = max(
        range(len(constrained_logits)), key=lambda i: constrained_logits[i]
    )

    # e. Condition d'arrêt (si le modèle génère le token de fin de séquence EOS)
    if next_token_id == model._tokenizer.eos_token_id:
        break

    # f. Ajouter le token sélectionné à la séquence pour l'étape suivante
    generated_ids.append(next_token_id)

# 3. Décoder le résultat final
final_text = model.decode(generated_ids)  # [cite: 253, 254]
print(final_text)
