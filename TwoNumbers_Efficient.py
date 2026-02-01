from typing import List

class solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap.update({num: i})

sol = solution()
print(sol.twoSum([3, 2, 4], 6))