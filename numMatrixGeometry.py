class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix: list[list[int]] = (
            [[0] * (len(matrix[0]) + 1)] +
            [[0] + row for row in matrix]
        )

        n: int = len(self.matrix)
        m: int = len(self.matrix[0])

        for r in range(1, n):
            prefix_sum: int = 0
            for c in range(m):
                above: int = self.matrix[r - 1][c]
                prefix_sum += self.matrix[r][c]
                self.matrix[r][c] = prefix_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        full_rectangle: int = self.matrix[row2][col2]
        top: int = self.matrix[row1 - 1][col2]
        left: int = self.matrix[row2][col1 - 1]
        add_area: int = self.matrix[row1 - 1][col1 - 1]

        return full_rectangle - top - left + add_area


sol = NumMatrix([[2, 2, 2],
                [2, 2, 2]])

# matrix = [[1] * 10_000 for _ in range(10_000)]

print(sol.sumRegion(0, 0, 1, 2))
