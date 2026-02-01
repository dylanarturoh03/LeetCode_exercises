class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            
            left: int = i + 1
            right: int = len(nums) - 1
            
            while left < right:
                
                sum = nums[i] + nums[left] + nums[right]
                
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return triplets
        
sol = Solution()
print(sol.threeSum([7, 8, 12, 5, 9, -3, -4, -12, -24, 50, 0]))