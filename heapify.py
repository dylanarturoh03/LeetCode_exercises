from typing import Optional
from trees import TreeNode, buildBT, printBT


class Solution:
    def max_heapify(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Max heapify a given complete binary tree.'''
        def sift_down(node: Optional[TreeNode]) -> None:
            '''Bubbles down the current value to it's correct position'''
            largest = node
            if node.left and node.left.val > largest.val:
                largest = node.left

            if node.right and node.right.val > largest.val:
                largest = node.right

            if largest != node:
                node.val, largest.val = largest.val, node.val
                sift_down(largest)

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return None

            # Heapify subtrees
            dfs(node.left)
            dfs(node.right)

            # Heapify current subtree
            sift_down(node)

        dfs(root)
        return root

    def min_heapify(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Min heapify a given complete binary tree.'''
        def sift_down(node: TreeNode) -> None:
            '''Bubbles down the current value to it's correct position'''
            smallest = node
            if node.left and node.left.val < smallest.val:
                smallest = node.left

            if node.right and node.right.val < smallest.val:
                smallest = node.right

            if smallest != node:
                node.val, smallest.val = smallest.val, node.val
                sift_down(smallest)

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return None

            # Heapify subtrees
            dfs(node.left)
            dfs(node.right)

            # Heapify current subtree
            sift_down(node)

        dfs(root)
        return root


bt = buildBT([1, 2, 3, 4, 5])
bt2 = buildBT([5, 4, 3, 2, 1])
printBT(bt, end=' ')
printBT(bt2)

sol = Solution()
printBT(sol.max_heapify(bt), end=' ')
printBT(sol.min_heapify(bt2))
