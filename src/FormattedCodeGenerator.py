import typing
from Token import Token
from Token import TokenCode
from TokenType import TokenType
import os


class FormattedCodeGenerator:
    def __init__(self):
        pass

    def generate(self, tokens: list[Token], save_path="output.html") -> None:
        try:
            os.remove(save_path) # remove the output if exists, will be appending to the file
        except OSError:
            pass
        with open(save_path, "a+") as f:
            self.add_header(f)
            for token in tokens:
                self.add_token(f, token)
            self.add_footer(f)

    def add_header(self, f: typing.TextIO) -> None:
        f.write('<link rel="stylesheet" href="color_scheme.css">')
        f.write('<div style="background: #272822; overflow:auto;width:auto;border:solid #272822;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">')

    def add_token(self, f: typing.TextIO, token: Token) -> None:
        token_type_to_css_class = {
            TokenType.RESERVED_KEYWORD: "reserved-keyword",
            TokenType.KNOWN_METHOD: "known-method",
            TokenType.NEW_DEFINITION: "new-definition",
            TokenType.CONSTANT: "constant",
            TokenType.STRING: "string",
            TokenType.SELF: "self",
            TokenType.COMMENT: "comment",
            TokenType.ERROR: "error",
            TokenType.OTHER: "other",
            TokenType.WHITE_CHARACTER: "white-character"
        }

        token_code_to_white_character = {
            TokenCode.SPACE: ' ',
            TokenCode.TAB: "&emsp;",
            TokenCode.NEWLINE: "<br>",
            TokenCode.EOF: ''
        }

        token_type = token.code.get_token_type()
        css_class = token_type_to_css_class[token_type]
        content = token.value
        if token_type == TokenType.WHITE_CHARACTER:
            content = token_code_to_white_character[token.code]
        if token_type != TokenType.COMMENT:
            content = content.replace('\t', '\\t')
            content = content.replace('\n', '\\n')
        else:
            content = content.replace('\t', "&emsp;")
            if content[-1] == '\n':
                content = ''.join(list(content)[:-1]) + "<br>"

        f.write(r'<span class="{}">{}</span>'.format(css_class, content))

    def add_footer(self, f: typing.TextIO) -> None:
        f.write("</pre></div>")
