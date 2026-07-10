"""
Main llm loop and model initialization
"""

from .constrained_decoder import ConstrainedDecoder
from .context_manager import ContextManager
from .json_format_constraint import JSONFormatConstraint


def main():

    context_manager = ContextManager(
        definitions_path="data/input/function_definitions.json"
    )

    schema_constraint = JSONFormatConstraint(
        available_functions=context_manager.get_functions()
    )


if __name__ == "__main__":
    main()
