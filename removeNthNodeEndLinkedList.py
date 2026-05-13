from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        '''
        Remove Nth node from end list in one pass
        by having a fixed gap between two pointers.
        '''
        # Algorithmic idea:
        # Creating two pointers with a fixed n + 1 gap so that by the time
        # lead pointer ends trail is just before the node to be deleted. Then,
        # we connect trail to trail.next.next and disconnect target from list.

        # The only edge case is when node to delete is the head, in which case
        # the dummy will handle it due to trail having a valid starting point
        # before head.

        # Guard in case n is clearly not valid.
        if n <= 0:
            printList(head)
            return head

        dummy: ListNode = ListNode(next=head)  # Dummy head handles edge case
        lead = trail = dummy
        counter: int = 0

        # Advance lead node until there is an n + 1 gap from dummy
        while lead and counter < n + 1:
            lead = lead.next
            counter += 1

        # If node to delete doesn't exist then return original.
        if counter < n + 1:
            printList(head)
            return head

        # Find nth node by having lead traverse the rest of list.
        while lead:
            lead = lead.next
            trail = trail.next

        # Disconnect target
        target = trail.next
        trail.next = trail.next.next
        target.next = None
        printList(dummy.next)
        return dummy.next


sol = Solution()
print(sol.removeNthFromEnd(buildList([1, 2, 3, 4, 5, 6]), 4))
