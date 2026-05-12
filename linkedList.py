from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildList(arr: list[int], idx: int = None) -> Optional[ListNode]:
    '''
        Build a linked list from an array and optionally
        create a cycle by attaching idx_node
        to the final node.
    '''
    # Algorithmic idea:
    # Create a series of n-Nodes and link
    # them through a series of implications in which
    # Head -> Node_1 -> Node_2... -> Node_n -> None
    dummy: ListNode = ListNode()  # Dummy gives us access to head
    current: ListNode = dummy
    cycleNode: Optional[ListNode] = None

    # Keep track of the index at each node in order to save the idx_node.
    counter: int = 0
    for val in arr:
        # For every element in the array
        # a new next node is created, said node
        # will be assigned a value arr[i]
        # then, the current nodes .next property
        # will start referencing the next node.
        next: ListNode = ListNode(val)
        current.next = next  # Link curr with next node.
        current = next  # Advance chain/list

        # If idx exists and the current node is the idx_node
        # we save the node for later.
        if idx is not None and counter == idx:
            cycleNode = current
        counter += 1

        # This algorithm is pretty much like holding
        # a real chain in the dark, because we are holding
        # the last link of the chain in order to not lose
        # it forever, then we grab a new link, attach it and
        # hold new last link to advance and repeat the process.

    # If there is a cycleNode the connection with last node is made.
    if cycleNode:
        current.next = cycleNode
    return dummy.next


def traverseList(head: Optional[ListNode]) -> None:
    '''Traverse a linked list while printing value flow.'''
    curr = head

    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next
    print(None)
