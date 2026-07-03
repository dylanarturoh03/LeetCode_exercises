from trees import Node


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def traverse(
            grid: list[list[int]],
            row: int,
            col: int,
            size: int
        ) -> int:
            '''
            Build quad tree by dividing grid into quadrants and
            building tree from the bottom-up.
            '''
            if size == 1:
                node = Node(
                    val=grid[row][col],
                    isLeaf=1,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )
                return node

            half = size // 2
            # Top left quad
            q1: Node = traverse(grid, row, col, half)
            # Top Right quad
            q2: Node = traverse(grid, row, col + half, half)
            # Bottom Left quad
            q3: Node = traverse(grid, row + half, col, half)
            # Bottom Right quad
            q4: Node = traverse(grid, row + half, col + half, half)

            isLeaf = q1.isLeaf and q2.isLeaf and q3.isLeaf and q4.isLeaf
            sameVal = q1.val == q2.val == q3.val == q4.val

            if isLeaf and sameVal:
                # Merge leaves and return a leaf node
                return Node(
                    val=q1.val,
                    isLeaf=1,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )

            val = q1.val if sameVal else 1
            # Create a parent, connect all the childrent to it
            # and return it.
            parent: Node = Node(
                val=val,
                isLeaf=0,
                topLeft=q1,
                topRight=q2,
                bottomLeft=q3,
                bottomRight=q4
            )
            return parent
        n = len(grid)
        return traverse(grid, 0, 0, n)


grid = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]

# grid = [[1, 0],
#         [1, 1]]

sol = Solution()
print(sol.construct(grid))
