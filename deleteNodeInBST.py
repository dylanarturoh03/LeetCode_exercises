from typing import Optional
from trees import TreeNode, buildBT, printBT


class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:
        '''
        Locate node and reorder the tree by inserting
        one of it's subtrees into the other.
        '''
        def insert(
            subtree: TreeNode,
            target: Optional[TreeNode]
        ) -> Optional[TreeNode]:
            '''Insert left subtree into leftmost position of right subtree.'''
            if target is None:
                return subtree
            target.left = insert(subtree, target.left)
            return target

        if root is None:
            return None

        if root.val == key:
            # Replace current node with one of the subtrees
            # if either the other is missing
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            # Insert left branch into right branch
            # make root.right branch the new root.
            return insert(root.left, root.right)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


bst = buildBT([5, 3, 9, 1, 4])
printBT(bst)
print()
sol = Solution()
printBT(sol.deleteNode(bst, 3))
