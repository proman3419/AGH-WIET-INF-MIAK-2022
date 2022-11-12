from Stream import Stream
from Scanner import Scanner
from TokenCode import TokenCode
from FormattedCodeGenerator import FormattedCodeGenerator


if __name__ == '__main__':
    with open("Stream.py", "r") as f:
        s = f.read()
    stream = Stream(s)
    scanner = Scanner(stream)

    tokens = []
    while True:
        token = scanner.scan()
        tokens.append(token)
        print(token, token.code)
        if token.code == TokenCode.EOF or token.code == TokenCode.ERROR:
            break

    formatted_code_generator = FormattedCodeGenerator()
    formatted_code_generator.generate(tokens)

    # TODO: proper scanning of strings and comments
    # probably 2 cases of white characters should be considered (for example ['\n'] and ['\', 'n'])
