import json


class FunctionsManager:

    def __init__(self):
        functions_file_path = "data/input/functions_definition.json"
        with open(functions_file_path, "r") as f:
            self.json_functions = json.load(f)

        wrapper = (
            "You are an expert system. Select the correct function name to satisfy the user request."
            "Available functions:")
        
        for item in self.json_functions.enumerate():
            wrapper += f"- {item["name"]} : {item["description"]}"

        wrapper += (
            "User Request: [METTRE_ICI_LE_PROMPT_DE_L_UTILISATEUR]"
            "The correct function to use is: fn_"
        )
