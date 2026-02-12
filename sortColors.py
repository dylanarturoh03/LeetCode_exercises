class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count: dict[int, int] = {0: 0,
                                 1: 0,
                                 2: 0}

        currentColor: int = 0

        for color in nums:
            count[color] += 1

        for i in range(len(nums)):
            while count[currentColor] == 0:
                currentColor += 1

            nums[i] = currentColor
            count[currentColor] -= 1


sol = Solution()
sol.sortColors(2, 2, 1, 1, 0, 2, 1, 0, 0, 2)
