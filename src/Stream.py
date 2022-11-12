class Stream:
    def __init__(self, data: str):
        self.data = data
        self.current_index = 0

    def get_char(self) -> str:
        if self.current_index >= len(self.data):
            return ''
        ch = self.data[self.current_index]
        self.current_index += 1
        return ch

    def peek_char(self) -> str:
        if self.current_index >= len(self.data):
            return ''
        return self.data[self.current_index]
