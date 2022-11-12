from enum import Enum, auto


class TokenType(Enum):
    RESERVED_KEYWORD = auto()
    KNOWN_METHOD = auto()
    NEW_DEFINITION = auto()
    CONSTANT = auto()
    STRING = auto()
    SELF = auto()
    COMMENT = auto()
    ERROR = auto()
    OTHER = auto()
    WHITE_CHARACTER = auto()
