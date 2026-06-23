from typing import Optional
from trees import TreeNode, buildBT, printBT


class Solution:
    def insertIntoBST(
        self,
        root: Optional[TreeNode],
        val: int
    ) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            nonlocal found

            if node.val > val:
                # Go down node.left
                dfs(node.left)

                if not found:
                    # Insert if reach empty space:
                    node.left = TreeNode(val=val)
                    found = True
            else:
                # Go down node.right
                dfs(node.right)

                if not found:
                    # Insert if reach empty space:
                    node.right = TreeNode(val=val)
                    found = True

        if not root:
            return TreeNode(val=val)

        found = False
        dfs(root)
        return root

    def insertIntoBST_Canonical(
        self,
        root: Optional[TreeNode],
        val: int
    ) -> Optional[TreeNode]:
        if not root:
            # Empty subtree: this is where the new node is inserted
            return TreeNode(val=val)

        # Recursively insert into the correct subtree
        # and reassign the updated subtree back to this node
        if root.val > val:
            # Rebuild left subtree with inserted value
            root.left = self.insertIntoBST_Canonical(root.left, val)
        else:
            # Rebuild right subtree with inserted value
            root.right = self.insertIntoBST_Canonical(root.right, val)

        # Return root of updated subtree
        return root


bst = buildBT([5, 3, 9, 1, 4])
sol = Solution()
# printBT(sol.insertIntoBST(bst, 6))
print()
printBT(sol.insertIntoBST_Canonical(bst, 6))
