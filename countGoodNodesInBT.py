from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxVal: int) -> int:
            if node is None:
                return 0
            if maxVal <= node.val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            return dfs(node.left, maxVal) + dfs(node.right, maxVal)
        return dfs(root, float('-inf'))


bt = buildBT([3, 3, None, 4, 2])
sol = Solution()
print(sol.goodNodes(bt))
