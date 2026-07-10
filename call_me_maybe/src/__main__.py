"""
Main llm loop and model initialization
"""

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .json_format_constraint import JSONFormatConstraint
from .test import Tester


def main():

    # By default pick the first question.
    test = Tester()
    test_input = test.gettest()

    context_manager = ContextManager()
    prompt = context_manager.get_prompt(test_input)

    constr_decod = ConstrainedDecoder()


if __name__ == "__main__":
    main()
