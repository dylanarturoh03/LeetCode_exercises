from typing import Optional
from linkedList import ListNode, buildList, printList


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Reorder linked list with n nodes into
        [1, n - 1, 2, n - 2, 3, n - 3, ...]
        '''
        def divideList() -> Optional[ListNode]:
            '''Finds middle node and disconnects it from first half.'''
            # The lists are split in half using the tortoise-hare algorithm
            # with addition of not just getting the middle, but also
            # disconnecting first from second half.
            slow = fast = head
            prev: Optional[ListNode] = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:  # If there is a half node -> Disconnect it from prev
                prev.next = None
            return slow

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            '''Reverse a given linked list.'''
            curr, prev = head, None

            while curr:
                nxt: Optional[ListNode] = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Algorithmic idea:
        # In order to efficiently rearrange the list
        # we must have easy access to each node's succesor.
        # Since normally you can't have fast access to any node
        # other than the original node.next, then the original list
        # must be modified in order to circumvent this limitation.

        # The form needed for efficiency is merge first half of list
        # with the reversed second half. The because both lists converge
        # to the middle element, which would be the last element in
        # either one or both lists (depending of odd / even list).

        # Split and reverse second half of list
        head2: Optional[ListNode] = reverseList(divideList())

        p1, p2 = head, head2
        prev: Optional[ListNode] = None

        # After the preprocessing has been done the merging process can begin.
        # Which consists of attaching current list 1 node to current list 2
        # node, then advancing both lists until list 1 has been exhausted.

        # Finally, in case list is odd we reconnect remaining node of list 2
        # with last node of reordered list.

        # In case it is not a single node or empty list
        if p1 != p2:
            # Due to the divide list process list 1 will always
            # have equal or fewer elements than list 2.
            while p1:
                nxt: Optional[ListNode] = p1.next
                p1.next = p2
                p1 = nxt

                prev = p2
                nxt = p2.next
                p2.next = p1
                p2 = nxt

            if p2:
                prev.next = p2

        printList(head)


sol = Solution()
print(sol.reorderList(buildList([1, 2, 3, 4, 5, 6])))
