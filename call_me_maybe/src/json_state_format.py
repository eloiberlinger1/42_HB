"""
Follow the generated tokens to guide the llm so it will choose JSON format characters when needed
"""


class JSONState:

    # Creer un enum plus tard pour gerer les differents etats json
    def __init__(self):
        self.states = {"WAIT_FOR_OPEN", "WAIT_FOR_KEY"}

        
