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


def printBT(root: Optional[TreeNode]) -> None:
    if root is None:
        return

    printBT(root.left)
    print(root.val, end=' ')
    printBT(root.right)
