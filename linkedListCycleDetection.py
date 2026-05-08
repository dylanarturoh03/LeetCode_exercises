from typing import Optional
from linkedList import ListNode, buildList


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''Detects an inner loop in a linked list O(N) time O(N) space.'''
        nodes: set[ListNode] = set()
        current = head
        # Algorithmic idea:
        # Save all nodes you visit into a set of nodes.
        # If at any point you come across a node you have
        # already seen, then you know there is a cycle.
        # Otherwise, the traversal will end naturally and return False.
        while current:
            if current in nodes:
                return True

            nodes.add(current)
            current = current.next
        return False

    def fastSlowPointers(self, head: Optional[ListNode]) -> bool:
        '''Detectes a cycle using fast slow pointers algorithm.'''
        # Algorithmic idea:
        # 2 pointers are defined:

        # Slow: Moves +1 at each step
        # Fast: MOes +2 at each step

        # They both start at the same point(head)
        # Since fast is always gonna be faster than slow, then the only
        # way for fast to meet slow ever again would be if there was a cycle.
        # Otherwise, fast will just arrive at null, finishing it's traversal.
        fast = slow = head

        # A = There is a cycle
        # B = Slow and fast meet.

        # This program works on the basis of A <-> B
        # If there is a cycle, then slow and fast meet.
        # If slow and fast meet, then there is a cycle.

        # Why?
        # Imagine C = len(cycle)
        # A -> B because fast is increasing it's d from slow by 1 at each step.
        # At some point there will be a difference of any multiple of C
        # between them or fast will exit the list.
        # Due to the fact C mod C = 0, then in a cycle having a difference of C
        # means being in the same position, if not, then no cycle.

        # B -> A
        # Easier to assume NOT(A), so if pointers meet, there is no cycle.
        # Try to prove it, but we realize fast ends the circuit in n/2 steps,
        # while slow in n steps.
        # Due to this in a straight line we know they will never meet.
        # Fast will always hit null first, so contradiction.
        # Which means... if A false, then B false.
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                # Here we prove there can be no cycle
                # because if the pointers didn't meet,
                # then there is no cycle.
                # We are proving the contrapositive, which
                # is equivalent to A -> B
                return False  # NOT B -> NOT A
            slow = slow.next

            if slow == fast:
                # Here, we know the pointers meet
                # so B, then A.
                # While, this is the converse, and generally wouldn't
                # be equivalent to A -> B, in this case B -> A is proven to
                # be true, so A -> B == B -> A
                return True  # B -> A


sol = Solution()
print(sol.fastSlowPointers(buildList([1, 2], -1)))
