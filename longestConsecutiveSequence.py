class Solution:
    def longestConsecutiveSequence(self, nums: list[int]) -> int:
        longestSequence = 0
        unvisitedNums = set(nums)

        for n in nums:
            auxSequence = 1

            auxSequence = self.countForward(n + 1, unvisitedNums, auxSequence)
            auxSequence = self.countBackwards(n - 1, unvisitedNums, auxSequence)


            if auxSequence > longestSequence:
                longestSequence = auxSequence
            
            if n in unvisitedNums:
                unvisitedNums.remove(n)

        return longestSequence
    
    def countForward(self, n: int, nums: set[int], auxSequence: int) -> int:
        if n not in nums:
            return auxSequence
        else :
            nums.remove(n)
            return self.countForward(n+1, nums, auxSequence+1)
    
    def countBackwards(self, n: int, nums: set[int], auxSequence: int) -> int:
        if n not in nums:
            return auxSequence
        else:
            nums.remove(n)
            return self.countBackwards(n-1, nums, auxSequence+1)

sol = Solution()
print(sol.longestConsecutiveSequence([0, -1]))