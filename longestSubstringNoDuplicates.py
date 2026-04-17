class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Algorithmic idea:
        # Go though the array building a window of valid chars
        # until a duplicate is found.
        # At that moment we implement a cutoff that logically invalidates
        # all values before it shrinking the valid window.
        # At each step we save the max length to then be returned.
        window: dict[str, int] = {}
        max_size: int = 0
        cutoff: int = 0
        # Invariant:
        # All elements in range of cutoff and i are currently valid.
        for i, char in enumerate(s):
            if char in window and window[char] >= cutoff:
                cutoff = window[char] + 1

            window[char] = i
            max_size = max(max_size, i - cutoff + 1)

        return max_size


sol = Solution()
print(sol.lengthOfLongestSubstring('To infinity and beyond'))
