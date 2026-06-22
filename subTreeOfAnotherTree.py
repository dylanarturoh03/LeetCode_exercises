from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:
        '''
            Identify potential candidates by pruning
            candidates with height + size + root.val
        '''
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            '''
                Traverse in DFS a given tree while computing height and size.

                If the subroot's height and size have been found
                subtree candidates are compared against the subroot.
            '''
            if not node:
                return 0, 0

            lh, ls = dfs(node.left)
            rh, rs = dfs(node.right)

            # If sub-tree has been found below, then abort traversal.
            if lh == -1 or rh == -1:
                return -1, -1

            size = 1 + ls + rs
            height = 1 + max(lh, rh)

            # If a potential candidate has been found,
            # then compare it to subRoot
            if (
                subRoot_h == height and
                node.val == subRoot.val and
                subRoot_s == size
            ):
                if isSameTree(node, subRoot):
                    return -1, -1
            return height, size

        def isSameTree(pN: Optional[TreeNode], qN: Optional[TreeNode]) -> bool:
            if pN is None and qN is None:
                return True
            if pN is None or qN is None or pN.val != qN.val:
                return False
            return (isSameTree(pN.left, qN.left) and
                    isSameTree(pN.right, qN.right))

        subRoot_h = subRoot_s = -1
        subRoot_h, subRoot_s = dfs(subRoot)
        return dfs(root) == (-1, -1)


bt, subBt = buildBT([3, 4, 5, 1, 2]), buildBT([4, 1, 2])
sol = Solution()
print(sol.isSubtree(bt, subBt))
