import json
import math
from llm_sdk import Small_LLM_Model


class JSONState:

    # Creer un enum plus tard pour gerer les differents etats json
    def __init__(self):
        self.states = {"WAIT_FOR_OPEN", "WAIT_FOR_KEY"}


model = Small_LLM_Model()

prompt = (
    "Select the correct function name to satisfy the user request.\n\n"
    "Available functions:\n"
    "- fn_add_numbers: Add two numbers together and return their sum.\n"
    "- fn_greet: Generate a greeting message for a person by name.\n\n"
    'User Request: "How much is 2 by 2?"\n\n'
    "The correct function to use is: fn_"
)
input_ids = model._tokenizer.encode(prompt, add_special_tokens=False)

max_new_tokens = 20
generated_ids = list(input_ids)

# vocab file : https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json
vocab_path = model.get_path_to_vocab_file()
with open(vocab_path, "r", encoding="utf-8") as f:
    vocab_dict = json.load(f)

id_to_token = {
    token_id: token_str for token_str, token_id in vocab_dict.items()
}

authorized_fonctions = [
    "fn_add_numbers",
    "fn_greet",
    "fn_reverse_string",
    "fn_get_square_root",
    "fn_substitute_string_with_regex",
]

for i in range(max_new_tokens):
    logits = model.get_logits_from_input_ids(generated_ids)

    #     90 =  "{"
    tokens_autorises = [90]

    constrained_logits = []

    for token_id, logit_value in enumerate(logits):
        if token_id in tokens_autorises:
            constrained_logits.append(logit_value)
        else:
            constrained_logits.append(-math.inf)

    next_token_id = max(
        range(len(constrained_logits)), key=lambda i: constrained_logits[i]
    )

    if next_token_id == model._tokenizer.eos_token_id:
        break

    generated_ids.append(next_token_id)

final_text = model.decode(generated_ids)

print("affichage de la reponse")

print(final_text)
