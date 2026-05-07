from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildList(arr: list[int]) -> Optional[ListNode]:
    '''Build a linked list from an array.'''
    # Algorithmic idea:
    # Create a series of n-Nodes and link
    # them through a series of implications in which
    # Head -> Node_1 -> Node_2... -> Node_n -> None
    dummy: ListNode = ListNode()  # Dummy gives us access to head
    current: ListNode = dummy

    for val in arr:
        # For every element in the array
        # a new next node is created, said node
        # will be assigned a value arr[i]
        # then, the current nodes .next property
        # will start referencing the next node.

        next: ListNode = ListNode(val)
        current.next = next  # Link curr with next node.
        current = next  # Advance chain/list

        # This algorithm is pretty much like holding
        # a real chain in the dark, because we are holding
        # the last link of the chain in order to not lose
        # it forever, then we grab a new link, attach it and
        # hold new last link to advance and repeat the process.
    return dummy.next
