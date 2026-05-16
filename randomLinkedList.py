from typing import Optional
from random import randrange


class Node:
    '''Create a random list node.'''
    def __init__(
        self,
        x: int,
        next: Optional['Node'] = None,
        random: Optional['None'] = None
    ):
        self.val = x
        self.next = next
        self.random = random


def buildRandomList(arr: list[int]) -> Optional[Node]:
    '''
    Create a random list from an array in one pass.

    Each node's `random` pointer is assigned to a randomly
    selected node (including possibly itself or None) from the list,
    determined independently for each node.
    '''
    # Algorithmic idea:
    # Create a random linked list by lazily creating nodes on-demand
    # and storing the index reference in a hash table.

    # Due to the fact any node could already be created at any point
    # we must check if the node we need is already present in the hash table
    # or not. If yes, then just grab it from there, if not create and store it
    # in case we ever need it again.

    # The hash table is key here, because it allows us to know if a given node
    # already exists or not, information which the algorithm uses to
    # create nodes on-demand.

    # nodes:
    # idx  -> Optional[Node]

    nodes: dict[int, Optional[Node]] = {}
    nodes[len(arr)] = None

    dummy: Node = Node(x=0)
    curr = dummy

    for i in range(len(arr)):
        # Check if nxt node to create exists in nodes.
        if i not in nodes:
            # If not, create it and store it.
            nodes[i] = Node(x=arr[i])

        idx: int = randrange(len(arr) + 1)  # Select random index from arr
        # Check if random node already exists.
        if idx not in nodes:
            # If not, then create it an store it.
            nodes[idx] = Node(x=arr[idx])

        # Now assign nxt to curr and rnd_node to nxt.

        # This because curr at the start is the dummy, and
        # we don't wanna waste an rnd_node there since this
        # will cause the last node to lack it's rnd_node.
        curr.next = nodes[i]
        curr.next.random = nodes[idx]
        curr = curr.next
        # print(curr.val, curr.random.val if curr.random else None)
    return dummy.next


def printRandomList(head: Optional[Node]) -> None:
    '''
    Print a random linked list by traversing it.

    The printing is done in a way (curr.val , curr.rnd pos) per node.
    Due to the lack of an initial index a first pass to assign them to
    every node must be done.

    The position of the rnd_node is 0-based.
    '''
    nodes: dict[Optional[Node], int] = {}
    nodes[None] = None
    counter = 0

    # Assign an index to every node in a hash table.
    curr = head
    while curr:
        nodes[curr] = counter
        curr = curr.next
        counter += 1

    # Print curr.val, curr.rnd pos per node.
    curr = head
    while curr:
        print(f'({curr.val}, {nodes[curr.random]})', end=' -> ')
        curr = curr.next
    print(None)
