from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        


class Solution:
    def _buildList(self, arr: list[Optional[int]]) -> Optional[ListNode]:
        '''Build a linked list from an array.'''
        if not arr:
            return None
        # Algorithmic idea:
        # Create a series of n-Nodes and link
        # them through a series of implications in which
        # Head -> Node_1 -> Node_2... -> Node_n -> None
        head = ListNode(arr[0])  # First element becomes the head
        current = head
        for i in range(1, len(arr)):
            # For every element in the array
            # a new node is created, said node
            # will be assigned a value arr[i]
            # then, the past nodes .next property
            # will start referencing the current node.
            nextNode: ListNode = ListNode(arr[i])
            current.next = nextNode  # Link nodes
            current = nextNode  # Advance the chain

            # This algorithm is pretty much like holding
            # a real chain in the dark, because we are holding
            # the last link of the chain in order to not lose
            # it forever, then we grab a new link, attach it and
            # hold new last link to advance and repeat the process.

        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Reverse singly linked list by using two (three) pointers.'''
        # A singly linked list is a list which can only go
        # from start to finish. You can't go back to a previous node
        # without restarting the search.

        # In order to re structure the list we must make the curr node
        # point to the past node.

        # Two problems come from this idea:
        # 1 - We can't go back to the prevous nude
        # 2 - The next node from curr may be lost forever

        # In order to circumvent this  we must hold on to next
        # and past nodes.

        # At beginning of the algorithm we set curr as the head, and past
        # as None, since we want the current head to poin to None. Then,
        # before cutting the chain between the next and current nodes we save
        # next, make curr point to the past node, and advance the chain by
        # update the curr node to be the past node, and the next node to be
        # curr node.

        # This repeats until curr node is null. At that point we return past
        # node since it is now the head of the current list.
        past: ListNode = None
        curr: ListNode = head

        while curr:
            next = curr.next  # Third pointer that holds on to next node
            curr.next = past  # Cut the chain, and link curr tu past node.
            past = curr  # advance past
            curr = next  # advance curr by using the saved next node.
        return past


sol = Solution()
print(sol.reverseList(sol._buildList([1, 2, 3, 4, 5])))
