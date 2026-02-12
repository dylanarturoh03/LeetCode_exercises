class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        currentRow, currentCol = row1, col1
        res: int = 0

        while currentRow <= row2:
            res += self.matrix[currentRow][currentCol]

            if currentCol == col2:
                currentCol = col1
                currentRow += 1
                continue

            currentCol += 1

        return res


# sol = NumMatrix([[3, 0, 1, 4, 2],
#                  [5, 6, 3, 2, 1],
#                  [1, 2, 0, 1, 5],
#                  [4, 1, 0, 1, 7],
#                  [1, 0, 3, 0, 5]])

matrix = [[1] * 10_000 for _ in range(10_000)]

sol = NumMatrix(matrix)

print(sol.sumRegion(0, 0, 9_999, 9_999))
