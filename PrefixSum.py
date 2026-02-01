class Solution:
    def prefixSumExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [0 for n in range(len(nums)+1)]
        suffix[len(suffix) - 1] = 1
        res = [0 for n in nums]
        # For each element of nums we sum the previous element in prefix,
        # which is the comulative amount up to that point,
        # with the current element in nums.
        # This loop is repeated until we have no more element left
        # to go through in nums.
        for i in nums:
            prefix.append(prefix[-1] * i)

        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        for i in range(len(nums)):
            L = prefix[i]
            R = suffix[i+1]
            res[i] = L * R

        return res


sol = Solution()
print(sol.prefixSumExceptSelf([1, 2, 4, 6]))