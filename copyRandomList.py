from typing import Optional
from randomLinkedList import Node, buildRandomList, printRandomList


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Deep-copies a linked list with random pointers using a hashmap.

        Maps each original node to its copy while traversing the list,
        creating nodes on demand so `next` and `random` pointers can be
        assigned in a single pass without duplication.
        """
        nodes: dict[Optional[Node], Optional[Node]] = {}
        nodes[None] = None

        dummy = Node(x=0)
        curr = dummy
        listNode = head

        while listNode:
            # Lazily create nodes on-demand so we can resolve random pointers
            if listNode not in nodes:
                nodes[listNode] = Node(x=listNode.val)

            if listNode.random not in nodes:
                nodes[listNode.random] = Node(x=listNode.random.val)

            curr.next = nodes[listNode]
            curr.next.random = nodes[listNode.random]
            curr = curr.next
            listNode = listNode.next
        return dummy.next

    def crl_cSpace(self, head: Optional[Node]) -> Optional[Node]:
        '''
        Deep-copy of a random list by inject copies of nodes into original list
        and then separating them.
        '''
        # Create copies of every node and inject them into list.
        curr = head

        while curr:
            copy: Node = Node(
                x=curr.val,
                next=curr.next,
                random=curr.random
            )
            curr.next = copy
            curr = copy.next

        # Reassign random pointer of copies to the correct nodes.
        curr = head.next if head else None

        while curr:
            curr.random = curr.random.next if curr.random else None
            curr = curr.next.next if curr.next else None

        # Separate lists.
        curr = head
        new_head = curr.next if curr else None

        while curr:
            copy = curr.next
            nxt = copy.next
            curr.next = nxt
            copy.next = nxt.next if nxt else None
            curr = curr.next
        return new_head


rndList = buildRandomList([1, 2, 3])
printRandomList(rndList)

sol = Solution()
# printRandomList(sol.copyRandomList(rndList))
printRandomList(sol.crl_cSpace(rndList))
