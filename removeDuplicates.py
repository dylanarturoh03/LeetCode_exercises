from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(len(nums)):
            
            if(nums[i] != nums[k]):
                k+=1
                nums[k] = nums[i]
        
        k+= 1

        return k

sol = Solution()
print(sol.removeDuplicates([1, 1, 3, 4, 5, 6]))

