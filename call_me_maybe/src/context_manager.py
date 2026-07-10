import json
import math
from llm_sdk import Small_LLM_Model


class ContextManager:

    def __init__(self):
        functions_file_path = "data/input/function_definitions.json"
        with open(functions_file_path, "r", encoding="utf-8") as f:
            self.json_functions = json.load(f)

    def get_prompt(self, user_request: str) -> str:
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
