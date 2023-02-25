class Stack:

    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in parentheses:
                # the if stack statement gets run if stack has a value
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        #         the not stack is true if
        #         stack is empty
        return True if not stack else False


class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min or self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
