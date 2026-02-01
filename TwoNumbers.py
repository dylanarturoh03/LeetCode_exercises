from typing import List

class Solution:


    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):

            for j, pos in enumerate(nums):
                
                #print(j)
                if i != j:
                    if num + pos == target:
                        print('Número actual: ' + str(num) + ' Números arreglo: ' + str(pos))
                        print(num + pos)
                        return[i, j]
                        

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
