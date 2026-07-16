from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Max path sum by computing the max path that passes through each node
        and bubbles up the best path to complement the parent.
        '''
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # Compute max sum path for both subtrees
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)
            total = node.val + leftSum + rightSum

            # Compare current best path to best path that includes current node
            self.maxSum = max(self.maxSum, total)

            # Return best path for parent
            return node.val + max(leftSum, rightSum)

        self.maxSum = float('-inf')
        dfs(root)
        return self.maxSum


bt = buildBT([-15, 10, 20, None, None, 15, 5, -5])
sol = Solution()
print(sol.maxPathSum(bt))
