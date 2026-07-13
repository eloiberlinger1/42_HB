import json


class Tester:
    """
    Darft just in order to test
    Later tasks :
        - Rename class as tests loader or smth
        - handle the input file from the user, ensure it follow the right format etc...
    """

    def __init__(self):
        self.testfile = "data/input/function_calling_tests.json"

    def gettest(self):
        with open(self.testfile, 'r') as f:
            self.json_file = json.load(f)

        return self.json_file[8]["prompt"]
