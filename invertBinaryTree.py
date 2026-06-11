from typing import Optional
from trees import TreeNode, buildBT, printBT


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Invert BT with post order recursive traversal.'''
        def helper(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            helper(node.left)  # Invert left subtree.
            helper(node.right)  # Invert right subtree.
            node.left, node.right = node.right, node.left  # Swap children
        helper(root)
        return root

    def invertTree_iter(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Invert BT with post order iterative traversal.'''
        stack = []
        node = root
        last_visited = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]

            if node.right is None or node.right == last_visited:
                # Swap children
                node.left, node.right = node.right, node.left
                last_visited = stack.pop()
                node = None
            else:
                node = node.right

        return root


bt = buildBT([1, 2, 3, 4, 5, 6, 7])
sol = Solution()
printBT(sol.invertTree(bt))
print()
printBT(sol.invertTree_iter(bt))
