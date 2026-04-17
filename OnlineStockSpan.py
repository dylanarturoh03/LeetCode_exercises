class StockSpanner:

    def __init__(self):
        self.monotonicStack: list[tuple[int, int]] = []
        self.spans: list[int] = []

    def next(self, price: int) -> int:
        span: int = 1

        while self.monotonicStack and price >= self.monotonicStack[-1][0]:
            span += self.monotonicStack[-1][1]
            self.monotonicStack.pop()

        self.monotonicStack.append((price, span))
        self.spans.append(span)
        return span

    def __repr__(self):
        return (
            f'Monotonic Stack: {self.monotonicStack}, Span Stack: {self.spans}'
        )

    def __str__(self):
        return f'{self.spans}'


obj = StockSpanner()
obj.next(100)
obj.next(80)
obj.next(60)
obj.next(70)
obj.next(60)
obj.next(75)
obj.next(85)
obj.next(101)
print(repr(obj))
