from typing import Optional
from trees import TreeNode, buildBT, printBT


class Solution:
    def removeLeafNodes(
        self, 
        root: Optional[TreeNode],
        target: int
    ) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not (node.left or node.right) and node.val == target:
                return None

            return node

        return dfs(root)


bt = buildBT([1, 2, 3, 5, 2, 2, 5])
sol = Solution()
printBT(sol.removeLeafNodes(bt, 2))
