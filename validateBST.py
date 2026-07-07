from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Validate BST by doing inorder traversal and
        checking if an increasing sequence is formed.
        '''
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            nonlocal prev
            if not dfs(node.left) or node.val <= prev:
                return False
            prev = node.val
            return dfs(node.right)
        prev = float('-inf')
        return dfs(root)


bt = buildBT([2, 1, 3])
sol = Solution()
print(sol.isValidBST(bt))
