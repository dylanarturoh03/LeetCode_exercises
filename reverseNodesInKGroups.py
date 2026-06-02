from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:
        '''
            Reverse K-groups within a given list by looking ahead,
            counting if there are enough nodes to complete a k-group
            and saving the nodes needed for reconnection after reversal.
        '''
        dummy = ListNode(next=head)
        leftAnchor = dummy
        curr = dummy.next

        while curr:
            # Look ahead
            groupHead = groupTail = curr
            for _ in range(k - 1):
                groupTail = groupTail.next
                if groupTail is None:
                    return dummy.next

            rightAnchor = groupTail.next

            # Reverse
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect
            leftAnchor.next = groupTail
            groupHead.next = rightAnchor

            leftAnchor = groupHead
        return dummy.next


sol = Solution()
printList(sol.reverseKGroup(buildList([1, 2, 3, 4, 5, 6]), 3))
