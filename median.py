def median(nums: list[int]) -> float:
    if not nums:
        return float('inf')

    nums.sort()

    left, right = 0, len(nums) - 1

    while left < right:
        left += 1
        right -= 1

    return (nums[left] + nums[right]) / 2


def median_constant(nums: list[int]) -> float:
    if not nums:
        return float('inf')

    n = len(nums)
    nums.sort()
    
    if not n % 2:
        return ((nums[n // 2]) + nums[(n // 2) - 1]) / 2
    else:
        return nums[(n - 1) // 2]


print(median_constant([1, 2, 3, 4, 5, 6, 7, 8]))
