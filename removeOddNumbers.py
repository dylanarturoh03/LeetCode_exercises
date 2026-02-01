from typing import List
class Solution:
    def removeOddNumbers(self, nums: List[int]) -> int:
        # Any non 0 number (even negatives) are a true in a boolean context

        k = 0

        for i in range(len(nums)):

            if not nums[i] % 2: # iF it is even
                nums[k] = nums[i] # Overwrite current position with the current read number
                k+=1 #Move to the next empty box, so to speak
        

        return k


sol = Solution()
print(sol.removeOddNumbers([2, 3, 5, 7, 9, 10, 3, 17, 12]))