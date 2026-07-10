from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(
            node: Optional[TreeNode],
            pos: int
        ) -> tuple[Optional[int], int]:
            '''Find kth smallest node by doing an inorder enumeration.'''
            if node is None:
                return None, pos

            lt, pos = dfs(node.left, pos)
            if lt is not None:
                return lt, pos

            if pos == k:
                return node.val, pos

            return dfs(node.right, pos + 1)
        ans, _ = dfs(root, 1)
        return ans


bst = buildBT([4, 3, 5, 2, None])
sol = Solution()
print(sol.kthSmallest(bst, 4))
