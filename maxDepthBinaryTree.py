from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''Get max depth of a given binary tree by recursively resolving the
            depth of the children subtrees.'''
        def helper(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            # At every node we assemble the answer by getting the longest path
            # legth of it's subtrees.
            return 1 + max(helper(node.left), helper(node.right))
        return helper(root)  # Note: In recursion the call is always the answer

    def maxDepth_sharedState(self, root: Optional[TreeNode]) -> int:
        '''
            Get max depth of a given binary tree by using recursive
            calls that count the depth and update a shared variable as they go.
        '''
        def helper(node: Optional[TreeNode], level: int) -> None:
            nonlocal longest_path

            if node is None:
                # When we reach the end just update the shared variable
                # if neccesary.
                longest_path = max(level, longest_path)
                return
            # In every node we explore all the node's subtrees
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        longest_path = 0
        helper(root, 0)
        return longest_path

    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        '''
            Get max depth of a tree by traversing it iteratibly,
            tracking the depth level of each node and updating longest_path
            at every downward step.
        '''
        stack = []
        longest_path = depth = 0
        node = root

        while stack or node:
            while node:
                depth += 1
                longest_path = max(depth, longest_path)
                stack.append((node, depth))
                node = node.left

            node, depth = stack.pop()
            node = node.right
        return longest_path


sol = Solution()
bt = buildBT([1, 2, 3, None, None, 4, None])
print(sol.maxDepth(bt))
print(sol.maxDepth_sharedState(bt))
print(sol.maxDepth_iterative(bt))
