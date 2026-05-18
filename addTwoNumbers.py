from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry: int = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            curr.next = ListNode(val=total % 10)
            carry = total // 10
            curr = curr.next
            l1, l2 = l1.next, l2.next

        rList: Optional[ListNode] = l2 if not l1 else l1

        while rList:
            total = rList.val + carry
            curr.next = ListNode(val=total % 10)
            carry = total // 10
            curr = curr.next
            rList = rList.next

        if carry:
            curr.next = ListNode(val=carry)
        return dummy.next


a = buildList([7, 0, 2, 9])
b = buildList([5, 0, 9])
sol = Solution()
printList(sol.addTwoNumbers(a, b))
