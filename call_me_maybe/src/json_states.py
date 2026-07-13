from enum import Enum, auto


class State(Enum):
    WAIT_FOR_OPEN_BRACE = auto()
    EXPECT_PROMPT_KEY = auto()
    READING_PROMPT_VALUE = auto()

    EXPECT_NAME_KEY = auto()
    READING_NAME_VALUE = auto()

    EXPECT_PARAMETERS_KEY = auto()  # literally expect ", "parameters": {
    EXPECT_PARAM_OPEN_BRACE = auto()

    EXPECT_PARAM_KEY = auto()  # expects the parameter name of the function ex :"number"
    READING_PARAM_VALUE = auto()
    EXPECT_PARAM_COMMA_OR_CLOSE = auto()

    EXPECT_CLOSE_BRACE = auto()
    DONE = auto()
