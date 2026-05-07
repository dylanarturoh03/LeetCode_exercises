from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _buildList(self, arr: list[int]) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        current: ListNode = dummy

        for val in arr:
            next: ListNode = ListNode(val)
            current.next = next
            current = next
        return dummy.next

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''Merge two sorted linked lists by creating a new list of n + m size.'''
        # Algorithmic idea:
        # Create a new list with m + n nodes.
        # Traverse both source lists and at each point compare node values
        # create a next node with the smaller value, advance the source list,
        # attach next node to tail node and move tail pointer to new node.

        # When one source list is fully traversed the other one will still
        # remain, so attach tail node to current node in the remaining list.
        # This will also attach all the subsequent nodes.

        # Key insight:
        # Create an empty dummy node, which will inevitably point to head node.
        # This because dummy node is just a placeholder.
        dummy: ListNode = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                next = ListNode(list1.val)
                list1 = list1.next
            else:
                next = ListNode(list2.val)
                list2 = list2.next
            curr.next = next
            curr = next

        remainingList: ListNode = list1 if not list2 else list2
        curr.next = remainingList
        return dummy.next


sol = Solution()
print(sol.merge(sol._buildList([1, 2, 4]), sol._buildList([1, 3, 4])))
