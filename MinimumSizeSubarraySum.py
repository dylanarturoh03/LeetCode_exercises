class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Algorithmic idea:
        # Build a window whose cummulative sum >= target.
        # Then, reduce it until it is lower than target
        # recording the min length.
        # After it is reduced, the process is repeated until
        # another valid window is built, or we have gone through
        # the entirety of nums.
        min_len: int = 0
        left: int = 0
        curr_sum: int = 0
        # Invariant:
        # The window grows while curr_sum < target
        # And shrinks while curr_sum >= target.
        for i, n in enumerate(nums):
            curr_sum += n

            while curr_sum >= target:
                # Initializes min_len with first valid window
                if left == 0:
                    min_len = i + 1
                else:
                    min_len = min(min_len, i - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len


sol = Solution()
print(sol.minSubArrayLen(5, [1, 4, 1]))
