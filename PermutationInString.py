class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Algorithmic idea:
        # Build a sliding window over s1 with size of at most len(s1).
        # At every step update the state of window
        # as characters come and go and compare it to the
        # frequency count of s1.
        s1_count: dict[str, int] = {}
        window: dict[str, int] = {}
        cutoff: int = 0  # Left boundary of the sliding window.

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        have, need = 0, len(s1_count)
        # Invariant:
        # After adjustment, the window size never exceeds len(s1).
        # window == frequency_map(s2[cutoff : i+1])
        for i, c in enumerate(s2):
            window[c] = window.get(c, 0) + 1

            if c in s1_count and s1_count[c] == window[c]:
                have += 1

            if i - cutoff + 1 > len(s1):
                exiting_char: str = s2[cutoff]
                if (exiting_char in s1_count and
                        s1_count[exiting_char] == window[exiting_char]):
                    have -= 1
                window[exiting_char] -= 1
                cutoff += 1

            if have == need:
                return True
        return False


sol = Solution()
print(sol.checkInclusion('abb', 'lcbabee'))
