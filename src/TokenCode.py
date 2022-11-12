from enum import Enum, auto
from TokenType import TokenType


class TokenCode(Enum):
    ERROR = auto()

    SPACE = auto()
    TAB = auto()
    NEWLINE = auto()
    EOF = auto()
    COMMENT = auto()

    PLUS = auto()
    ADD_MODIFY = auto()
    MINUS = auto()
    SUBTRACT_MODIFY = auto()
    TYPING_RETURN = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER = auto()
    GREATER_OR_EQUAL = auto()
    LESS = auto()
    LESS_OR_EQUAL = auto()

    COLON = auto()
    SEMICOLON = auto()
    COMMA = auto()
    PERIOD = auto()
    STRING = auto()
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
    FROM = auto()
    IMPORT = auto()
    PASS = auto()
    RETURN = auto()
    TRY = auto()
    EXCEPT = auto()
    FINALLY = auto()
    RAISE = auto()

    DEF = auto()
    CLASS = auto()
    SELF = auto()

    PRINT = auto()

    def is_reserved(token_value: str) -> bool:
        return token_value in TokenCode._value2member_map_

    def get_token_type(self) -> TokenType:
        token_code_to_token_type = {
            TokenCode.ERROR: TokenType.ERROR,

            TokenCode.SPACE: TokenType.WHITE_CHARACTER,
            TokenCode.TAB: TokenType.WHITE_CHARACTER,
            TokenCode.NEWLINE: TokenType.WHITE_CHARACTER,
            TokenCode.EOF: TokenType.WHITE_CHARACTER,
            TokenCode.COMMENT: TokenType.COMMENT,

            TokenCode.PLUS: TokenType.RESERVED_KEYWORD,
            TokenCode.ADD_MODIFY: TokenType.RESERVED_KEYWORD,
            TokenCode.MINUS: TokenType.RESERVED_KEYWORD,
            TokenCode.SUBTRACT_MODIFY: TokenType.RESERVED_KEYWORD,
            TokenCode.TYPING_RETURN: TokenType.RESERVED_KEYWORD,
            TokenCode.MULTIPLY: TokenType.RESERVED_KEYWORD,
            TokenCode.DIVIDE: TokenType.RESERVED_KEYWORD,
            TokenCode.ASSIGN: TokenType.RESERVED_KEYWORD,
            TokenCode.EQUAL: TokenType.RESERVED_KEYWORD,
            TokenCode.NOT_EQUAL: TokenType.RESERVED_KEYWORD,
            TokenCode.GREATER: TokenType.RESERVED_KEYWORD,
            TokenCode.GREATER_OR_EQUAL: TokenType.RESERVED_KEYWORD,
            TokenCode.LESS: TokenType.RESERVED_KEYWORD,
            TokenCode.LESS_OR_EQUAL: TokenType.RESERVED_KEYWORD,

            TokenCode.COLON: TokenType.OTHER,
            TokenCode.SEMICOLON: TokenType.OTHER,
            TokenCode.COMMA: TokenType.OTHER,
            TokenCode.PERIOD: TokenType.OTHER,
            TokenCode.STRING: TokenType.STRING,
            TokenCode.LEFT_PARENTHESIS: TokenType.OTHER,
            TokenCode.RIGHT_PARENTHESIS: TokenType.OTHER,
            TokenCode.LEFT_BRACKET: TokenType.OTHER,
            TokenCode.RIGHT_BRACKET: TokenType.OTHER,
            TokenCode.LEFT_BRACE: TokenType.OTHER,
            TokenCode.RIGHT_BRACE: TokenType.OTHER,

            TokenCode.NUMBER: TokenType.CONSTANT,
            TokenCode.ID: TokenType.OTHER,

            TokenCode.IF: TokenType.RESERVED_KEYWORD,
            TokenCode.NOT: TokenType.RESERVED_KEYWORD,
            TokenCode.FOR: TokenType.RESERVED_KEYWORD,
            TokenCode.WHILE: TokenType.RESERVED_KEYWORD,
            TokenCode.BREAK: TokenType.RESERVED_KEYWORD,
            TokenCode.CONTINUE: TokenType.RESERVED_KEYWORD,
            TokenCode.FROM: TokenType.RESERVED_KEYWORD,
            TokenCode.IMPORT: TokenType.RESERVED_KEYWORD,
            TokenCode.PASS: TokenType.RESERVED_KEYWORD,
            TokenCode.RETURN: TokenType.RESERVED_KEYWORD,
            TokenCode.TRY: TokenType.RESERVED_KEYWORD,
            TokenCode.EXCEPT: TokenType.RESERVED_KEYWORD,
            TokenCode.FINALLY: TokenType.RESERVED_KEYWORD,
            TokenCode.RAISE: TokenType.RESERVED_KEYWORD,

            TokenCode.DEF: TokenType.NEW_DEFINITION,
            TokenCode.CLASS: TokenType.NEW_DEFINITION,
            TokenCode.SELF: TokenType.SELF,

            TokenCode.PRINT: TokenType.KNOWN_METHOD
        }

        return token_code_to_token_type[self]
