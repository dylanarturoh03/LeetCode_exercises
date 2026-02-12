def merge(left: list[int], right: list[int]) -> list[int]:
    res: list[int] = []
    l: int = 0
    r: int = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    res += left[l:]
    res += right[r:]

    return res


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    half: int = len(nums) // 2
    left: list[int] = merge_sort(nums[:half])
    right: list[int] = merge_sort(nums[half:])

    return merge(left, right)


print(merge_sort([1, 0, 0, 0, 0, 0]))
