class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i: int = 1
        k: int = 0

        while i < len(nums):
            while i < len(nums) and nums[i] == nums[k]:
                i += 1

            if i >= len(nums):
                break

            k += 1

            if k != i:
                nums[k] = nums[i]

            i += 1

        return k + 1


sol = Solution()
print(sol.removeDuplicates([1, 2, 3, 4, 5, 6, 7]))
