from typing import Optional
from linkedList import ListNode


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.cnt = 0
        self.dummy: Optional[ListNode] = ListNode()
        self.tail: Optional[ListNode] = self.dummy

    def enQueue(self, value: int) -> bool:
        '''Add new element to list and keep track of tail.'''
        if self.isFull():
            return False

        self.cnt += 1

        self.tail.next = ListNode(value, self.dummy.next)
        self.tail = self.tail.next
        self.tail.next = self.dummy.next
        return True

    def deQueue(self) -> bool:
        '''
            deQueues old head and tries to look for the next node.
            If none is found then revert to original state of list.
        '''
        if self.isEmpty():
            return False

        self.cnt -= 1

        # Extract old head and look for new head
        old_head = self.dummy.next
        new_head = old_head.next if old_head != old_head.next else None

        if not new_head:
            # Revert back to original empty state.
            self.tail = self.dummy
        else:
            # Make tail point to new head.
            self.tail.next = new_head
        self.dummy.next = new_head
        old_head.next = None
        return True

    def Front(self) -> int:
        return self.dummy.next.val if self.dummy.next else - 1

    def Rear(self) -> int:
        return self.tail.val if self.tail != self.dummy else - 1

    def isEmpty(self) -> bool:
        return self.dummy.next is None

    def isFull(self) -> bool:
        return self.cnt == self.k


obj = MyCircularQueue(3)
obj.enQueue(3)
obj.enQueue(5)
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
