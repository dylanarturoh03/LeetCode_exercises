def maxSum(arr: list[int]) -> int:
    max_sum, current_sum = arr[0], arr[0]
    for n in arr[1:]:
        current_sum = max(current_sum + n, n)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(maxSum([4, -10, 2, 3, -100]))
