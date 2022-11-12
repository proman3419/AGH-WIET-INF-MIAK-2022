from Stream import Stream
from Scanner import Scanner
from TokenCode import TokenCode


if __name__ == '__main__':
    s = """from Stream import Stream
from Scanner import Scanner
from TokenCode import TokenCode


if __name__ == '__main__':
    s = "13+17-(5+23*2++)+2329++a123b+b{}"
    stream = Stream(s)
    scanner = Scanner(stream)

    while True:
        token = scanner.scan()
        print(token)
        if token.token_code == TokenCode.EOF or token.token_code == TokenCode.ERROR:
            break
"""
    stream = Stream(s)
    scanner = Scanner(stream)

    while True:
        token = scanner.scan()
        print(token)
        if token.token_code == TokenCode.EOF or token.token_code == TokenCode.ERROR:
            break
