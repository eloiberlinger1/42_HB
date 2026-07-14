"""
Main llm loop and model initialization
"""

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .functions_schema import FunctionSchema
from .json_logits_processor import JSONLogitsProcessor
from .json_state_manager import JSONStateManager
from llm_sdk import Small_LLM_Model

from .test import Tester


def main():

    # By default pick the first question.
    test = Tester()
    raw_prompt = test.gettest()

    context_manager = ContextManager()
    prompt = context_manager.get_prompt(raw_prompt)

    model = Small_LLM_Model()

    functions_path = "data/input/functions_definition.json"
    schema = FunctionSchema(functions_path)
    state_manager = JSONStateManager(target_prompt=raw_prompt, schema=schema)
    json_processor = JSONLogitsProcessor(model, state_manager)

    decoder = ConstrainedDecoder(model, json_processor)

    result = decoder.generate(prompt)

    print("Finish")
    print(result)


if __name__ == "__main__":
    main()
