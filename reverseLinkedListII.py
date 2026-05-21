from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:
        '''
        Reverse a segment inside a given linked list in one pass.

        Identify the sublist, keep anchors to the left segment, the soon
        to be tail of left < right, reverse it and reconnect all 3 sections.

        In order to do it an achor to these 4 nodes must be present:
        - Tail left segment
        - Head reversed segment
        - Tail reversed segment
        - Head right segment

        During the final reconnection this flow is followed:
        TLS -> HRevS -> ... -> TRevS -> HRS
        '''
        dummy = ListNode(next=head)
        curr = dummy

        # Find left boundary.
        for _ in range(0, left - 1):
            curr = curr.next
        preNode = curr
        leftNode = preNode.next

        # Reverse sublist [right, left]
        curr = leftNode
        prev = None
        for _ in range(left, right + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reconnect all segments.
        preNode.next = prev
        leftNode.next = curr
        return dummy.next


sol = Solution()
list: Optional[ListNode] = buildList([1, 2, 3, 4, 5])

printList(sol.reverseBetween(list, 2, 5))
