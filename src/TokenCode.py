from enum import Enum, auto


class TokenCode(Enum):
    ERROR = auto()
    SPACE = auto()
    TAB = auto()
    NEWLINE = auto()
    EOF = auto()

    PLUS = auto()
    ADD_MODIFY = auto()
    MINUS = auto()
    SUBTRACT_MODIFY = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    COLON = auto()
    SEMICOLON = auto()
    COMMA = auto()
    PERIOD = auto()
    SINGLE_QUOTE = auto()
    DOUBLE_QUOTE = auto()
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()

    NUMBER = auto()
    ID = auto()

    IF = auto()
    NOT = auto()
    FOR = auto()
    WHILE = auto()
    BREAK = auto()
    CONTINUE = auto()

    PRINT = auto()
    FROM = auto()
    IMPORT = auto()

    # def is_reserved(token_value: str) -> bool:
    #     return token_value in TokenCode._value2member_map_
