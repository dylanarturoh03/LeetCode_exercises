from typing import Optional
from trees import TreeNode, printBT


class Solution:
    def buildTree(
        self,
        preorder: list[int],
        inorder: list[int]
    ) -> Optional[TreeNode]:
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            '''
            Reconstruct binary tree from preorder and inorder
            traversals using divide & conquer.
            '''
            # Key idea:
            # Preorder gives us the node creation order
            # Inorder gives us the neighbors and overall structure

            if left > right:
                return None

            # Consume next node from preorder
            rootVal = preorder[self.pos]
            node = TreeNode(val=rootVal)
            self.pos += 1

            # Find root boundaries in inorder
            rootPos = roots[rootVal]
            del roots[rootVal]

            # Construct subtrees
            node.left = dfs(left, rootPos - 1)
            node.right = dfs(rootPos + 1, right)

            return node

        roots = {inorder[i]: i for i in range(len(inorder))}
        self.pos = 0
        return dfs(0, len(preorder) - 1)


preorder = [1, 2, 3, 4]
inorder = [2, 1, 3, 4]

sol = Solution()
printBT(sol.buildTree(preorder, inorder))
