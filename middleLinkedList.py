from typing import Optional
from linkedList import ListNode, buildList


class Solution:
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Find middle or uppermiddle node in a straight list.'''
        slow = fast = head
        # Algorithmic idea:
        # Since the tortoise-hare algorithm lives off of the 2:1 ration between
        # slow and fast, then fast finishes list in n/2 steps roughtly meaning
        # slow ends in n steps. Due to this, by the time fast hits null, then
        # slow will be in n/2 node.

        # Outer loop maintains 2:1 ratio at all times
        # If we can no longer make a full 2-step then
        # the loop is over.
        while fast and fast.next:
            # The loop handles nicely the two end positions before exit.
            # These are last node, or second to last node.
            # If we fast lands in last node we know the list odd and
            # slow is exactly in the middle node of list.
            # If it lands in second to last, then the list is even
            # and next iteration slow will be in upper-middle node.
            fast = fast.next.next
            slow = slow.next
        return slow


sol = Solution()
print(sol.findMiddle(buildList([1, 2, 3, 4, 5, 6])))
