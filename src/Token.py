from TokenCode import TokenCode


class Token:
    def __init__(self, code: TokenCode, value: str):
        self.code = code
        self.value = value

    def __str__(self) -> str:
        return str((self.code.name, self.value))
