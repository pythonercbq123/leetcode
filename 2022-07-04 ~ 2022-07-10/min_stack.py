class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        elif x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def min(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return -1
