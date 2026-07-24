from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right


# Definition of a QuadTree node.
class Node:
    def __init__(
        self,
        val: int,
        isLeaf: int,
        topLeft: Optional['Node'] = None,
        topRight: Optional['Node'] = None,
        bottomLeft: Optional['Node'] = None,
        bottomRight: Optional['Node'] = None
    ) -> None:
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def buildBT(arr: list[int]) -> Optional[TreeNode]:
    '''Build binary tree from a given array.'''
    def helper(idx: int) -> Optional[TreeNode]:
        if len(arr) <= idx or arr[idx] is None:
            return None
        node = TreeNode(
            val=arr[idx],
            left=helper(2 * idx + 1),
            right=helper(2 * idx + 2)
        )
        return node
    return helper(0)


def printBT(root: Optional[TreeNode], end='\n') -> None:
    '''Print a given BT in preorder.'''
    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return

        print(node.val, end=' ')
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    print(end=end)
