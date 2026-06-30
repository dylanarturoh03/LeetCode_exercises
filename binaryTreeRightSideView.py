from typing import Optional
from collections import deque
from trees import TreeNode, buildBT


class Solution:
    '''Save the rightmost element of every level.'''
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        '''Iterative breadth-first-search traversal'''
        if root is None:
            return []

        q = deque([root])
        res = []

        while q:
            # For every level save the rightmost element
            res.append(q[-1].val)
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
        return res

    def rsv_DFS(self, root: Optional[TreeNode]) -> list[int]:
        '''Recursive depth-first-search traversal'''
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return

            # If we have reached a new depth save the node
            if depth == len(res):
                res.append(node.val)

            # Explore right to find rightmost first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        res = []
        dfs(root, 0)
        return res


bt = buildBT([1, 2, 3, 4, None, None, None, 5])
sol = Solution()
print(sol.rightSideView(bt))
print(sol.rsv_DFS(bt))
