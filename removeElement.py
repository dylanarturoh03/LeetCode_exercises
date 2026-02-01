from typing import List

class Solution:
    def removeElements(self, nums: List[int], val: int) -> int :
        k = 0

        for read in range(len(nums)):
            
            if nums[read] != val:
                nums[k] = nums[read]
                k+=1
                

        print(nums)
        return k
            
sol = Solution()
print(sol.removeElements([3, 2, 1, 3, 4, 5, 7, 3, 9], 3))