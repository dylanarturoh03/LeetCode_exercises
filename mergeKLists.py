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

    def mergeKLists_divideConquer(
        self,
        lists: list[Optional[ListNode]]
    ) -> Optional[ListNode]:
        '''
            Merge K-lists by divide & conquer array and merging both halves.
        '''
        def merge(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
            '''Merge two given ordered linked lists.'''
            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    nxt = list1
                    list1 = list1.next
                else:
                    nxt = list2
                    list2 = list2.next

                curr.next = nxt
                curr = curr.next

            rList = list1 if not list2 else list2

            curr.next = rList
            return dummy.next

        if len(lists) <= 1:
            return lists[0] if lists else None

        mid = len(lists) // 2
        fHalf = self.mergeKLists_divideConquer(lists[:mid])
        sHalf = self.mergeKLists_divideConquer(lists[mid:])
        return merge(fHalf, sHalf)


sol = Solution()
lists = [buildList([1, 2, 4]), buildList([1, 3, 5]), buildList([3, 6])]
printList(sol.mergeKLists_divideConquer(lists))
