"""
Main llm loop and model initialization
"""

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .functions_schema import FunctionSchema
from .json_logits_processor import JSONLogitsProcessor
from .json_state_manager import JSONStateManager
from llm_sdk import Small_LLM_Model
import json


    
class Main:
    """
    Darft just in order to test
    Later tasks :
        - Rename class as tests loader or smth
        - handle the input file from the user, ensure it follow the right format etc...
    """

    def __init__(self):
        self.prompts_file = "data/input/function_calling_tests.json"
        self.output_file = "data/output/function_calling_results.json"
        self.functions_path = "data/input/functions_definition.json"
        self.model = Small_LLM_Model()
        self.schema = FunctionSchema(self.functions_path)
        

    def _run_prompt(self, raw_prompt: str) -> dict:
        context_manager = ContextManager()
        prompt = context_manager.get_prompt(raw_prompt)

        model = self.model

        schema = self.schema
        state_manager = JSONStateManager(target_prompt=raw_prompt, schema=schema)
        json_processor = JSONLogitsProcessor(model, state_manager)

        decoder = ConstrainedDecoder(model, json_processor)

        result = decoder.generate(prompt)
        result_json = json.loads(result)
        return result_json
        
    def write_result(self, results: list) -> None:
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4)
        except Exception:
            print("Failed to save results :(")

    def run(self):
        try:
            with open(self.prompts_file, 'r') as f:
                self.json_file = json.load(f)
        except Exception:
            print("Failed to open inputs file :(")

        results = []

        for p in self.json_file:
            try:
                results.append(self._run_prompt(p['prompt']))

            except Exception:
                print("An error occured. Make sure your file respect required format")
        
        self.write_result(results)


if __name__ == "__main__":
    main = Main()
    main.run()
