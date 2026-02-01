class Solution:
    def maxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount: int = 0
        auxCount: int = 0

        for n in nums:

            if n == 1:
                auxCount += 1
                maxCount = max(auxCount, maxCount)
            else:
                auxCount = 0

        return maxCount


sol = Solution()
print(sol.maxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
