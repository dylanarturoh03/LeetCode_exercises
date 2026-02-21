class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        quadruplets: list[list[int]] = []
        nums.sort()

        for i, base in enumerate(nums):
            if i > 0 and base == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left: int = j + 1
                right: int = len(nums) - 1

                while left < right:
                    four_sum: int = base + nums[j] + nums[left] + nums[right]

                    if four_sum < target:
                        left += 1
                    elif four_sum > target:
                        right -= 1
                    else:
                        quadruplets.append(
                            [base, nums[j], nums[left], nums[right]])

                        left += 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return quadruplets


sol = Solution()
print(sol.fourSum([1, -1, 1, -1, 1, -1, 1, 4, 2, 1], 3))
