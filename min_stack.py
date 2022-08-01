class MinStack:

    def __init__(self):
        self.stack = []
        self.min_item = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_item[-1] if self.min_item else val)
        self.min_item.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_item.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_item[-1]  