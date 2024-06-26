class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


output = []

m = MinStack()  # []
m.push(-2)      # [-2]
m.push(0)       # [-2, 0]
m.push(-1)      # [-2, 0, -1]
print("(A)", m.top())      # will return -1
print("(B)", m.getMin())   # will return -2
m.pop()         # [-2, 0]
print("(C)", m.top())      # will return 0
print("(D)", m.getMin())   # will return -2
