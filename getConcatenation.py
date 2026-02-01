class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] * (2 * len(nums))

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + len(nums)] = n

        return ans


sol = Solution()
print(sol.getConcatenation([1, 2, 3]))
