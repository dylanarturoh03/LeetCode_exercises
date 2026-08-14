from abc import ABC, abstractmethod
from typing import Optional, Protocol, TypeVar


CT = TypeVar('CT', bound='Comparable')


class Comparable(Protocol):

    def __lt__(self: CT, other: CT) -> bool:
        ...


class BinaryHeap[T: Comparable](ABC):

    def __init__(self, arr: Optional[list[T]]):
        self._heap: list[T] = [] if arr is None else arr
        self.heapify()

    def __len__(self) -> int:
        return len(self._heap)

    def __iter__(self):
        return iter(self._heap)

    def __repr__(self) -> str:
        return str(self._heap)

    def __reversed__(self):
        return reversed(self._heap)

    def push(self, item: T) -> None:
        '''Push a new item to heap'''
        self._heap.append(item)
        self._sift_up(len(self._heap) - 1)

    def pop(self) -> T:
        '''Pop current root.'''
        if not self._heap:
            raise IndexError('pop from empty heap')

        self._swap(0, len(self._heap) - 1)

        popped = self._heap.pop()

        self._sift_down()
        return popped

    def peek(self) -> T:
        '''Peek current root.'''
        if not self._heap:
            raise IndexError('peek from empty heap')

        return self._heap[0]

    def replace(self, item: T) -> T:
        '''Replace and pop current root with a given value.'''
        old_root = self.peek()
        self._heap[0] = item
        self._sift_down()

        return old_root

    def heapify(self) -> None:
        '''Heapify self.heap'''
        for i in range((len(self._heap) - 2) // 2, -1, -1):
            self._sift_down(i)

    def _sift_down(self, idx: int = 0) -> None:
        '''
        Bubble-down element present in a given
        index to it's correct position.
        '''
        n = len(self._heap)
        best = curr = idx
        while True:
            left = curr * 2 + 1
            if n > left and self._cmp(left, best):
                best = left

            right = curr * 2 + 2
            if n > right and self._cmp(right, best):
                best = right

            if best == curr:
                break

            self._swap(curr, best)
            curr = best

    def _sift_up(self, idx: int) -> None:
        '''
        Bubble-up element present in a given
        index to it's correct position.
        '''
        curr = idx

        while curr > 0:
            p = (curr - 1) // 2
            if not self._cmp(curr, p):
                break

            self._swap(curr, p)
            curr = p

    def _swap(self, i: int, j: int) -> None:
        '''Swap values of positions i and j within heap.'''
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    @abstractmethod
    def _cmp(self, cand: int, best: int) -> bool:
        '''Determine if element pos[cand] is better than pos[best].'''
        pass


class MinHeap[T: Comparable](BinaryHeap[T]):
    def __init__(self, arr: Optional[list[T]] = None):
        super().__init__(arr)

    def _cmp(self, cand: int, best: int) -> bool:
        return self._heap[cand] < self._heap[best]


class MaxHeap[T: Comparable](BinaryHeap[T]):
    def __init__(self, arr: Optional[list[T]] = None):
        super().__init__(arr)

    def _cmp(self, cand: int, best: int) -> bool:
        return self._heap[best] < self._heap[cand]
