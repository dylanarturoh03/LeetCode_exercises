from typing import Optional
from collections import deque
from trees import TreeNode, buildBT


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Perform a breadth-first traversal of the tree,
        processing one level at a time.
        """
        if root is None:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            res.append(level)
        return res


bt = buildBT([1, 2, 3, 4, 5, 6, 7])
# bt = buildBT([])
sol = Solution()
print(sol.levelOrder(bt))
