matrix: list[list[int]] = [[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12],
                           [13, 14, 15, 16]]

# for arr in matrix:
#     arr.insert(0, 0)

# top: list[int] = [0 for _ in range(len(matrix[0]))]

# matrix.insert(0, top)


new_matrix = (
    [[0] * (len(matrix[0]) + 1)] +
    [[0] + row for row in matrix]
)

n = len(new_matrix)
m = len(new_matrix[0])

for r in range(1, n):
    prefix_sum = 0
    for c in range(m):
        above = new_matrix[r - 1][c]
        prefix_sum += new_matrix[r][c]
        new_matrix[r][c] = prefix_sum + above

for row in new_matrix:
    print(row)
