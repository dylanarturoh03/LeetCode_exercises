from trees import TreeNode, buildBT


class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:
        def dfs(node: TreeNode) -> TreeNode:
            '''Traverse a given BST looking for LCA of p and q.'''
            # Base case:
            # Either we have reached P or Q
            if node.val == p.val or node.val == q.val:
                return node

            # Determine next move to reach both nodes
            nextPN = node.left if node.val > p.val else node.right
            nextQN = node.left if node.val > q.val else node.right

            # return if paths divert
            if nextPN != nextQN:
                return node
            # Keep looking if same path
            return dfs(nextPN)
        return dfs(root)


bst = buildBT([5, 3, 8, 1, 4, 7, 9, None, 2])
p, q = TreeNode(val=3), TreeNode(val=8)

sol = Solution()
print(sol.lowestCommonAncestor(bst, p, q))
