import json

"""
You are an expert system. Select the correct function name to satisfy the user request.

Available functions:
- fn_add_numbers: Add two numbers together and return their sum.
- fn_greet: Generate a greeting message for a person by name.
- fn_reverse_string: Reverse a string and return the reversed result.
- fn_get_square_root: Calculate the square root of a number.
- fn_substitute_string_with_regex: Replace all occurrences matching a regex pattern in a string.

User Request: "[METTRE_ICI_LE_PROMPT_DE_L_UTILISATEUR]"

The correct function to use is: fn_
"""


class FunctionsManager:

    def __init__(self):
        self.functions_file_path = "data/input/functions_definition.json"
        self.json_functions = json()
        with open(self.functions_file_path, "r") as f:
            self.json_functions = json.decoder(f)
