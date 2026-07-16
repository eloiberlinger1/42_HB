"""
Main llm loop and model initialization
"""

import argparse
import glob
import json
import os
from tabnanny import verbose

from llm_sdk import Small_LLM_Model

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .functions_schema import FunctionSchema
from .json_logits_processor import JSONLogitsProcessor
from .json_state_manager import JSONStateManager
from .logger import set_verbose


class Main:
    """
    Darft just in order to test
    Later tasks :
        - Rename class as tests loader or smth
        - handle the input file from the user,
            ensure it follow the right format etc...
    """

    def __init__(
            self,
            prompts_file: str,
            output_file: str,
            functions_path: str,
    ):
        self.prompts_file = prompts_file
        self.output_file = output_file
        self.functions_path = functions_path
        self.model = Small_LLM_Model()
        self.schema = FunctionSchema(self.functions_path)

    def _run_prompt(self, raw_prompt: str) -> dict:
        context_manager = ContextManager()
        prompt = context_manager.get_prompt(raw_prompt)

        model = self.model

        schema = self.schema
        state_manager = JSONStateManager(
            target_prompt=raw_prompt,
            schema=schema
        )
        json_processor = JSONLogitsProcessor(model, state_manager)

        decoder = ConstrainedDecoder(model, json_processor)

        result = decoder.generate(prompt)
        result_json = json.loads(result)
        return result_json

    def write_result(self, results: list) -> None:

        output_dir = os.path.dirname(self.output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4)
        except Exception:
            print("Failed to save results :(")
            exit(1)

    def run(self):
        try:
            with open(self.prompts_file, 'r') as f:
                self.json_file = json.load(f)
        except Exception:
            print("Failed to open inputs file :(")
            exit(1)

        results = []

        for p in self.json_file:
            try:
                results.append(self._run_prompt(p['prompt']))

            except Exception:
                print(
                    "An error occured.",
                    " Make sure your file respect required format")
                exit(1)

        self.write_result(results)


def get_default_file(keyword: str, fallback: str) -> str:
    """
    Looks for input files
    We expect the names for the prompts file contains
        "calling" and "definition" for functions definition
    """
    search_pattern = os.path.join("data", "input", f"*{keyword}*.json")
    files_found = glob.glob(search_pattern)

    if files_found:
        return files_found[0]
    else:
        raise Exception
    return fallback


if __name__ == "__main__":

    try:
        default_input = get_default_file(
            "calling",
            "data/input/function_calling_tests.json"
        )
        default_functions = get_default_file(
            "definition",
            "data/input/functions_definition.json"
        )
    except Exception:
        print("\nNo input file found\n")
        exit(1)
    default_output = "data/output/function_calling_results.json"

    parser = argparse.ArgumentParser(
        description="Call Me Maybe - Constrained Decoding for LLM"
    )
    parser.add_argument(
        "--input",
        type=str,
        default=default_input,
        help="File containing prompts"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Display token generation infos"
    )
    parser.add_argument(
        "--functions_definition",
        type=str,
        default=default_functions,
        help="Path to the definition of the functions to use")
    parser.add_argument(
        "--output",
        type=str,
        default=default_output,
        help="Output file"
    )

    args = parser.parse_args()
    set_verbose(args.verbose)

    main = Main(
        prompts_file=args.input,
        output_file=args.output,
        functions_path=args.functions_definition,
    )
    main.run()
