from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            Get diameter of a tree by getting the max of the longest path's
            of all nodes.
        '''
        def getHeight(node: Optional[TreeNode]) -> int:
            '''
                Return height of a given subtree and
                cache it for later computation.
            '''
            if node is None:
                return 0

            if node in memo:
                return memo[node]

            height = 1 + max(getHeight(node.left), getHeight(node.right))
            memo[node] = height
            return height

        memo = {}
        stack = []
        curr = root
        diameter = 0

        # For every node compute it's longest path
        # and update diameter if necessary
        while stack or curr:
            while curr:
                diameter = max(
                    getHeight(curr.left) + getHeight(curr.right),
                    diameter
                )
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right
        return diameter

    def diameterBT_canonical(self, root: Optional[TreeNode]) -> int:
        '''
            Calculate diameter of a given BT by
            calculating the height of all subtrees and
            at the same time using that data to get the
            longest path that passes through each node.

            Update diameter as you find a longer path.
        '''
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal diameter
            lh, rh = dfs(node.left), dfs(node.right)
            diameter = max(lh + rh, diameter)
            return 1 + max(lh, rh)

        diameter: int = 0
        dfs(root)
        return diameter


bt = buildBT([1, 2, 3, 4, 5, 6, 7])
sol = Solution()
print(sol.diameterOfBinaryTree(bt))
print(sol.diameterBT_canonical(bt))
