from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    '''Tree traversals with iterative methods'''
    def preOrder(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], []
        node = root

        while stack or node:
            while node:
                # descend left as far as possible
                res.append(node.val)  # visit root node
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right  # process right branches
        return res

    def inOrder(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], []
        node = root

        while stack or node:
            while node:
                # descend left as far as possible
                stack.append(node)
                node = node.left
            node = stack.pop()  # visit root node
            res.append(node.val)
            node = node.right  # process right branches
        return res

    def postOrder(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], []
        node = root
        last_visited = None

        while stack or node:
            while node:
                # descend left as far as possible
                stack.append(node)
                node = node.left
            node = stack[-1]
            # if we have visited the right branches or they don't exist:
            if node.right == last_visited or node.right is None:
                # visit Root
                res.append(node.val)
                last_visited = stack.pop()
                node = None
            else:
                # process right subtree
                node = node.right
        return res


sol = Solution()
bt = buildBT([1, 2, 3])
print(sol.postOrder(bt))
