class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if not nums:
            return False

        increasing: bool = True
        decreasing: bool = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
                break
        
        if increasing:
            return True

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                decreasing = False
                break

        return decreasing


sol = Solution()
print(sol.isMonotonic([1, 3, 2]))
