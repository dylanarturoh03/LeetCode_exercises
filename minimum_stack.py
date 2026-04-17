class MinStack:
    '''Create a separate stack structure that track
    min val at each step.'''
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    def __repr__(self):
        return f'stack: {self.stack}, minStack: {self.min_stack}'

    def __str__(self):
        return f'{self.stack}'


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(repr(minStack))
minStack.pop()
print(repr(minStack))
