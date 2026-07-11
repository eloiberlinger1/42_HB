"""
Main llm loop and model initialization
"""

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .json_format_constraint import JSONFormatConstraint
from llm_sdk import Small_LLM_Model

from .test import Tester


def main():

    # By default pick the first question.
    test = Tester()
    test_input = test.gettest()

    context_manager = ContextManager()
    prompt = context_manager.get_prompt(test_input)

    json_formater = JSONFormatConstraint()

    model = Small_LLM_Model()
    decoder = ConstrainedDecoder(model, json_formater)

    result = decoder.generate(prompt)

    print("Finish")
    print(result)


if __name__ == "__main__":
    main()
