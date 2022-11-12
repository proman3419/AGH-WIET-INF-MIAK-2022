from TokenCode import TokenCode


class Token:
    def __init__(self, token_code: TokenCode, value: str):
        self.token_code = token_code
        self.value = value

    def __str__(self) -> str:
        return str((self.token_code.name, self.value))
