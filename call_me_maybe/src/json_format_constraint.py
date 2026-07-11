"""
Follow the generated tokens to guide the llm so it will choose JSON format characters when needed
"""


class JSONState:
    pass


class JSONFormatConstraint:

    # Creer un enum plus tard pour gerer les differents etats json
    def __init__(self):
        self.states = {"WAIT_FOR_OPEN", "WAIT_FOR_KEY"}

    def get_allowed_tokens(self, generated_ids):

        print(generated_ids)

        return "{"
