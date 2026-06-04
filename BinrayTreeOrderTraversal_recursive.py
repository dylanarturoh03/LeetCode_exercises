from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    '''Tree traversals with recursive methods.'''
    def inOrder(self, root: Optional[TreeNode]) -> list[int]:
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            helper(node.left)
            res.append(node.val)
            helper(node.right)

        res = []
        helper(root)
        return res

    def preOrder(self, root: Optional[TreeNode]) -> list[int]:
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            res.append(node.val)
            helper(node.left)
            helper(node.right)

        res = []
        helper(root)
        return res

    def postOrder(self, root: Optional[TreeNode]) -> list[int]:
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            helper(node.left)
            helper(node.right)
            res.append(node.val)

        res = []
        helper(root)
        return res


sol = Solution()
bt = buildBT([1, 2, 3, 4, 5, 6, 7])
print(sol.inOrder(bt))
print(sol.preOrder(bt))
print(sol.postOrder(bt))
