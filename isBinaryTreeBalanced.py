from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            Determine if a given tree is balanced by recursively computing the
            height of each node's subtrees and computing the difference.
        '''
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # Compute height of subtrees
            lh, rh = dfs(node.left), dfs(node.right)

            # if one of the subtrees is unbalanced abort
            if lh == -1 or rh == -1:
                return -1

            # if the current subtree is unbalanced abort
            if abs(lh - rh) > 1:
                return -1

            return 1 + max(lh, rh)  # Otherwise, return normal height
        return dfs(root) != -1


bt = buildBT([1, 2, 3, None, None, 4])
sol = Solution()
print(sol.isBalanced(bt))
