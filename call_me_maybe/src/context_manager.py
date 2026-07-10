import json
import math


class ContextManager:

    def __init__(self, definitions_path="data/input/functions_definition.json"):
        """
        Load all the functions from the functions file.
        """

        with open(definitions_path, "r", encoding="utf-8") as f:
            self.json_functions = json.load(f)

    def get_prompt(self, user_request: str) -> str:
        """
        Wrap the functions of the class in a prompt
        to guide the model and tell him to pick the most adapted function.
        """
        wrapper = (
            "You are an expert system. Select the correct function name and "
            "parameters to satisfy the user request.\n\n"
            "Available functions:\n"
        )

        for item in self.json_functions:
            wrapper += f"- {item['name']}: {item['description']}\n"

        wrapper += (
            f'\nUser Request: "{user_request}"\n\n'
            "Output the result as a strict JSON object following the schema.\n"
            "Response: "
        )
        return wrapper
