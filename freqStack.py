class FreqStack:
    '''O(N) time complexity on every operation.'''

    def __init__(self):
        self.stack: list[int] = []
        self.freq: dict[int, int] = {}
        self.buffer_stack: list[int] = []
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        self._get_buffer_elems()
        self.stack.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1
        self.max_freq = max(self.freq[val], self.max_freq)

    def pop(self) -> int:
        self._get_buffer_elems()

        while self.stack and self.freq[self.stack[-1]] < self.max_freq:
            self.buffer_stack.append(self.stack.pop())

        self.freq[self.stack[-1]] = self.freq[self.stack[-1]] - 1
        self.max_freq = self._get_max()
        if self.freq[self.stack[-1]] == 0:
            del self.freq[self.stack[-1]]
        return self.stack.pop()

    def _get_max(self) -> int:
        return max(self.freq.values())

    def _get_buffer_elems(self) -> None:
        while self.buffer_stack:
            self.stack.append(self.buffer_stack.pop())

    def __repr__(self):
        return (
            f'Stack: {self.stack}\n'
            f'Freq: {self.freq}\n'
            f'Buffer stack: {self.buffer_stack}\n'
            f'Max freq: {self.max_freq}'
        )

    def __str__(self):
        return f'{self.stack + self.buffer_stack[::-1]}'

    def __len__(self):
        return len(self.stack) + len(self.buffer_stack())


class FreqStack_2():

    def __init__(self):
        self.freqs: dict[int, int] = {}
        self.buckets: dict[int, list[int]] = {}
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        self.freqs[val] = self.freqs.get(val, 0) + 1
        f = self.freqs[val]
        if f not in self.buckets:
            self.buckets[f] = []
        self.buckets[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        val: int = self.buckets[self.max_freq].pop()
        if not self.buckets[self.max_freq]:
            self.max_freq -= 1
        self.freqs[val] -= 1
        return val

    def __repr__(self):
        return (
            f'freqs: {self.freqs}\n'
            f'buckets: {self.buckets}\n'
            f'max_freq: {self.max_freq}'
        )

    def __str__(self):
        return f'{[
            x for bucket in self.buckets.values() for x in bucket
        ]}'


obj = FreqStack_2()
obj.push(8)
obj.push(7)
obj.push(7)
obj.push(6)
obj.push(5)
obj.push(4)
obj.push(3)
obj.pop()
obj.push(7)
print(obj.__repr__())
print(obj)
