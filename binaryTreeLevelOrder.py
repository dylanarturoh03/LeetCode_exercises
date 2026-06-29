from typing import Optional
from trees import TreeNode, buildBT
from queue import Queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        '''
            Traverse given BT with a breath first search algorithm.
            While you process nodes you add it's children to the queue
            along with their depth.
        '''
        if root is None:
            return []

        q = Queue()
        res = []
        q.put((root, 1))

        while not q.empty():
            # Dequeue node at front
            curr, level = q.get()
            if len(res) < level:
                # Create new nested list for current level
                res.append([])
            # Add curent's nodes value to latest sublist
            res[-1].append(curr.val)
            # Add children along with their level
            if curr.left:
                q.put((curr.left, level + 1))
            if curr.right:
                q.put((curr.right, level + 1))
        return res


bt = buildBT([1, 2, 3, 4, 5, 6, 7])
# bt = buildBT([])
sol = Solution()
print(sol.levelOrder(bt))
