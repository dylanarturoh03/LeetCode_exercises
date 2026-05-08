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


sol = Solution()
print(sol.hasCycle(buildList([1, 2, 3, 4], 1)))
