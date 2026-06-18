from typing import Optional
from trees import TreeNode, buildBT


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
            Determine if two given BT's are the same by recursively
            traversing them at the same time and comparing both structure
            and values as you descend.
        '''
        def dfs(pN: Optional[TreeNode], qN: Optional[TreeNode]) -> bool:
            # If both were able to traverse the whole path
            if pN is None and qN is None:
                return True
            # If either structure or values differe
            if pN is None or qN is None or pN.val != qN.val:
                return False
            return dfs(pN.left, qN.left) and dfs(pN.right, qN.right)
        return dfs(p, q)

    def isSameTree_iter(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
     ) -> bool:
        '''
            Determine if two given BT's are the same by traversing them
            iteratively at the same time and comparing both structure
            and values as you descend.
        '''
        pStack, qStack = [], []
        pNode, qNode = p, q

        while pStack or qStack or pNode or qNode:
            while pNode and qNode:
                if pNode.val != qNode.val:
                    return False

                pStack.append(pNode)
                qStack.append(qNode)
                pNode, qNode = pNode.left, qNode.left

            if pNode or qNode:
                return False

            pNode, qNode = pStack.pop(), qStack.pop()
            pNode, qNode = pNode.right, qNode.right
        return True


p, q = buildBT([1, 2, 3]), buildBT([1, 2, 3, 5])
sol = Solution()
print(sol.isSameTree(p, q))
print(sol.isSameTree_iter(p, q))
