class Solution():
    def containsDuplicates(self, nums: list[int]) -> bool:
        seen = {}
        duplicate = False

        for i in range(len(nums)):
            
            if nums[i] in seen:
                duplicate = True
                break
            
            seen[nums[i]] = i

        return duplicate
    
sol = Solution()
print(sol.containsDuplicates([3, 4, 3]))
