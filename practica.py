from typing import Optional
from linkedList import ListNode, buildList, printList


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


def isHappy(n: int) -> bool:
    def squareSums(num: int) -> int:
        res = 0
        while num:
            res += (num % 10) ** 2
            num //= 10
        return res

    slow = fast = n

    while True:
        slow = squareSums(slow)
        fast = squareSums(squareSums(fast))

        if fast == 1:
            return True

        if fast == slow:
            return False


def reorderList(head: Optional[ListNode]) -> Optional[ListNode]:
    def findMiddle() -> Optional[ListNode]:
        fast = slow = head
        past = None
        while fast and fast.next:
            past = slow
            slow = slow.next
            fast = fast.next.next
        if past:
            past.next = None
        return slow

    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        past = None

        while curr:
            nxt = curr.next
            curr.next = past
            past = curr
            curr = nxt
        return past

    head2 = reverseList(findMiddle())
    list1, list2 = head, head2

    while list1 and list2:
        nxt = list1.next
        list1.next = list2
        list1 = nxt

        past = list2
        nxt = list2.next
        list2.next = list1
        list2 = nxt
    if list2:
        past.next = list2
    return head


printList(reorderList(buildList([1, 2, 3, 4, 5])))
