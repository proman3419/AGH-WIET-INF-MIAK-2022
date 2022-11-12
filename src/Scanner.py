from Stream import Stream
from TokenCode import TokenCode
from Token import Token


class Scanner:
    def __init__(self, stream: Stream):
        self.stream = stream

    def scan(self) -> Token:
        ch = self.stream.get_char()
        if ch == '':
            return Token(TokenCode.EOF, "EOF")
        if ch == ' ':
            return Token(TokenCode.SPACE, ch)
        if ch == '\t':
            return Token(TokenCode.TAB, ch)
        if ch == '\n':
            return Token(TokenCode.NEWLINE, ch)
        if ch == '+':
            if self.stream.peek_char() == '=':
                ch += self.stream.get_char()
                return Token(TokenCode.ADD_MODIFY, ch)
            return Token(TokenCode.PLUS, ch)
        if ch == '-':
            if self.stream.peek_char() == '=':
                ch += self.stream.get_char()
                return Token(TokenCode.SUBTRACT_MODIFY, ch)
            return Token(TokenCode.MINUS, ch)
        if ch == '*':
            return Token(TokenCode.MULTIPLY, ch)
        if ch == '/':
            return Token(TokenCode.DIVIDE, ch)
        if ch == '=':
            if self.stream.peek_char() == '=':
                ch += self.stream.get_char()
                return Token(TokenCode.ASSIGN, ch)
            return Token(TokenCode.EQUAL, ch)
        if ch == '!':
            if self.stream.peek_char() == '=':
                ch += self.stream.get_char()
                return Token(TokenCode.NOT_EQUAL, ch)
            return Token(TokenCode.ERROR, ch)
        if ch == ':':
            return Token(TokenCode.COLON, ch)
        if ch == ';':
            return Token(TokenCode.SEMICOLON, ch)
        if ch == ',':
            return Token(TokenCode.COMMA, ch)
        if ch == '.':
            return Token(TokenCode.PERIOD, ch)
        if ch == "'":
            return Token(TokenCode.SINGLE_QUOTE, ch)
        if ch == '"':
            return Token(TokenCode.DOUBLE_QUOTE, ch)
        if ch == '(':
            return Token(TokenCode.LEFT_PARENTHESIS, ch)
        if ch == ')':
            return Token(TokenCode.RIGHT_PARENTHESIS, ch)
        if ch == '[':
            return Token(TokenCode.LEFT_BRACKET, ch)
        if ch == ']':
            return Token(TokenCode.RIGHT_BRACKET, ch)
        if ch == '{':
            return Token(TokenCode.LEFT_BRACE, ch)
        if ch == '}':
            return Token(TokenCode.RIGHT_BRACE, ch)
        if ch.isdigit():
            while self.stream.peek_char().isdigit():
                ch += self.stream.get_char()
            return Token(TokenCode.NUMBER, ch)
        if ch.isalpha() or ch == '_':
            while self.stream.peek_char().isdigit() or self.stream.peek_char().isalpha() or self.stream.peek_char() == '_':
                ch += self.stream.get_char()
            if ch == "if":
                return Token(TokenCode.IF, ch)
            if ch == "not":
                return Token(TokenCode.NOT, ch)
            if ch == "for":
                return Token(TokenCode.FOR, ch)
            if ch == "while":
                return Token(TokenCode.WHILE, ch)
            if ch == "break":
                return Token(TokenCode.BREAK, ch)
            if ch == "continue":
                return Token(TokenCode.CONTINUE, ch)
            if ch == "print":
                return Token(TokenCode.PRINT, ch)
            if ch == "from":
                return Token(TokenCode.FROM, ch)
            if ch == "import":
                return Token(TokenCode.IMPORT, ch)
            return Token(TokenCode.ID, ch)
        return Token(TokenCode.ERROR, ch)
