from typing import Optional


class MyQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = 0
        self.queue = []

    def front(self) -> int:
        '''Peek front value.'''
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def rear(self) -> int:
        '''Peek rear value.'''
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def enQueue(self, value: int) -> bool:
        '''Append value to queue is possible.'''
        if self.isFull():
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        '''Logically remove front value from queue by shifting head pointer.'''
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head += 1

        # Compact self.queue when memory leak is as big as the valid elements
        if len(self.queue) >= (len(self.queue) - self.head) * 2:
            self.queue = self.queue[self.head:]
            self.head = 0
        return True

    def isEmpty(self) -> bool:
        return len(self.queue) - self.head == 0

    def isFull(self) -> bool:
        return len(self.queue) - self.head == self.k


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.tail = -1
        self.head = self.c = 0
        self.queue: list[Optional[int]] = [None] * k

    def front(self) -> int:
        '''Peek front value.'''
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def rear(self) -> int:
        '''Peek rear value.'''
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def enQueue(self, value: int) -> bool:
        '''Shift tail poitner and assigne value to it's position.'''
        if self.isFull():
            return False

        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        self.c += 1
        return True

    def deQueue(self) -> bool:
        '''
            Logically remove front value from queue and shifting head pointer.
        '''
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        self.head = (self.head + 1) % self.k
        self.c -= 1
        return True

    def isEmpty(self) -> bool:
        return self.c == 0

    def isFull(self) -> bool:
        return self.c == self.k


obj = MyCircularQueue(5)
print(obj.queue)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.enQueue(5))
print(obj.queue)
print(obj.head, obj.tail)
