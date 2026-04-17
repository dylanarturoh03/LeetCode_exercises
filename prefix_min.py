def get_grade(num: float | int) -> str:
    return (
        'S' if num == 10 else
        'A' if num >= 9 else
        'B' if num >= 8 else
        'C' if num >= 7 else
        'D' if num >= 6 else
        'E' if num >= 5 else
        'F'
    )


def prefix_mean(nums: list[int | float]) -> list[str]:
    prefix_sum: float | int = 0.0
    prefix_average: list[str] = [''] * len(nums)
    for i in range(len(prefix_average)):
        if nums[i] > 10:
            raise ValueError('Students must not have over the max (10)')
        prefix_sum += nums[i]
        prefix_average[i] = get_grade(prefix_sum / (i + 1))
    return prefix_average


print(prefix_mean([5, 10, 10, 10, 10]))
