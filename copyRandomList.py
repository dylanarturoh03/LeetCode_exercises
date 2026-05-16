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


rndList = buildRandomList([1, 2, 3, 4, 5, 6, 7])
printRandomList(rndList)

sol = Solution()
printRandomList(sol.copyRandomList(rndList))
