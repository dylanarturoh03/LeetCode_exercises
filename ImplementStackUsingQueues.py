from collections import deque


class MyStack:

    def __init__(self):
        self.q1: deque[int] = deque()
        self.q2: deque[int] = deque()

    def push(self, x: int) -> None:
        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError('pop from an empty stack.')
        # q: deque[int] = self.q1 if not self.q2 else self.q2
        # empty_q: deque[int] = self.q2 if q is self.q1 else self.q1

        q, empty_q = self._current_q_state()

        while len(q) > 1:
            empty_q.append(q.popleft())
        return q.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError('peek from an empty stack.')
        # q: deque[int] = self.q1 if not self.q2 else self.q2
        # empty_q: deque[int] = self.q2 if q is self.q1 else self.q1

        q, empty_q = self._current_q_state()
        top_element: int = 0

        while q:
            top_element = q[0]
            empty_q.append(q.popleft())
        return top_element

    def _current_q_state(self) -> tuple[deque[int], deque[int]]:
        if self.q1:
            return self.q1, self.q2
        return self.q2, self.q1

    def empty(self) -> bool:
        return not self.q1 and not self.q2

    def __repr__(self):
        return f'Q1: {self.q1}, Q2: {self.q2}'

    def __str__(self) -> str:
        return f'{list(self.q1 or self.q2)}'

    def __len__(self) -> int:
        return len(self.q1 or self.q2)


class MyStack2:

    def __init__(self):
        self.q: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.pop())

    def pop(self) -> int:
        if self.empty():
            raise IndexError('pop from an empty stack.')
        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError('peek from an empty stack.')
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

    def __repr__(self) -> str:
        return f'{self.q}'

    def __str__(self) -> str:
        return f'{list(self.q)[::-1]}'

    def __len__(self) -> int:
        return len(self.q)


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(len(obj))
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
print(repr(obj))
# param_2 = obj.pop()
# param_3 = obj.top()
# obj.push(3)
# param_4 = obj.empty()
# print(obj)
# print(len(obj))
