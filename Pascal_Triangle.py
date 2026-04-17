class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = []
        # Algorithmic idea:
        # We generate pascal's triangle
        # with n rows.

        # This is a bottom-up dynamic programming solution.

        # We start from the smallest subproblem (row 0),
        # and iteratively construct each row using the previously computed row.
        # Each internal element at position (i, j) is computed as:
        # triangle[i-1][j-1] + triangle[i-1][j].
        for i in range(numRows):
            row: list[int] = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    # The first and last elements of each row
                    # are base cases and are always 1.
                    row.append(1)
                    continue
                n1: int = triangle[i - 1][j - 1]
                n2: int = triangle[i - 1][j]
                row.append(n1 + n2)
            triangle.append(row)
        return triangle


sol = Solution()
print(sol.generate(6))
