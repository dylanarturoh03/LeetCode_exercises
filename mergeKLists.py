from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def mergeKLists(
        self,
        lists: list[Optional[ListNode]]
    ) -> Optional[ListNode]:
        '''
            Merge K lists by manually finding the min node in lists
            and merging it with merged list.
        '''
        dummy = ListNode()
        curr = dummy

        while True:
            minNode: Optional[ListNode] = ListNode(val=float('inf'))
            nList: int = -1
            for i, node in enumerate(lists):
                if node and node.val < minNode.val:
                    minNode = node
                    nList = i

            if minNode.val == float('inf'):
                break

            nxt = minNode.next
            curr.next = minNode
            curr = curr.next
            lists[nList] = nxt

        return dummy.next


sol = Solution()
lists = [buildList([1, 2, 4]), buildList([1, 3, 5]), buildList([3, 6])]
printList(sol.mergeKLists(lists))
