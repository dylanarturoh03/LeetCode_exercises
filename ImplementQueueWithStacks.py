class MyQueue:
    def __init__(self):
        self.stack: list[int] = []

    def push(self, x: int) -> None:
        '''Simulate FIFO by reversing self.stack using an auxiliary stack'''
        aux_stack: list[int] = []

        for _ in range(len(self.stack)):
            aux_stack.append(self.stack.pop())

        self.stack.append(x)

        for _ in range(len(aux_stack)):
            self.stack.append(aux_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack

    def __str__(self) -> str:
        return f'{self.stack}'


class MyQueue2:
    def __init__(self):
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not (self.in_stack or self.out_stack)

    def _move(self) -> None:
        '''Move elements to the out_stack only when necessary (when empty).'''
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def __repr__(self):
        return f'in_stack: {self.in_stack}, out_stack: {self.out_stack}'

    def __str__(self):
        return f'{self.out_stack[::-1] + self.in_stack}'

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue2()
obj.push(1)
obj.push(2)
obj.push(3)
obj.peek()
obj.push(4)
obj.pop()
print(len(obj))
print(repr(obj))
print(obj)
