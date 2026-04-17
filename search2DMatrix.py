class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def toIndex(cell: tuple[int, int]) -> int:
            row, col = cell
            return row * numCols + col

        def toCell(idx: int) -> tuple[int, int]:
            return idx // numCols, idx % numCols

        numCols: int = len(matrix[0])
        low, high = 0, toIndex((len(matrix) - 1, numCols - 1))

        while low <= high:
            mid: int = (high + low) >> 1
            midRow, midCol = toCell(mid)
            midCellVal: int = matrix[midRow][midCol]

            if midCellVal > target:
                high = mid - 1
            elif midCellVal < target:
                low = mid + 1
            else:
                return True
        return False


sol = Solution()
print(sol.searchMatrix([[1, 1, 2],
                        [5, 6, 7]],
                       5))
