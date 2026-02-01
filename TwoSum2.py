class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, num in enumerate(nums):
                
            if target - num in seen:
                return [seen.get(target - num), i]
            
            seen[num] = i

sol = Solution()
print(sol.twoSum([4, 5, 6], 10))    