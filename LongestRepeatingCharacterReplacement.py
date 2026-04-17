class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Algorithmic idea:
        # Construct and update a window where the number of
        # replaceable characters is <= k.
        # As it evolves keep track of maximum size reached.
        max_freq: int = 0
        max_size: int = 0
        count: dict[str, int] = {}
        start: int = 0
        # Invariant:
        # The number of replaceable elements inside window
        # is always <= k.
        for i, c in enumerate(s):
            # Update window
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])

            # Shink if neccesary
            while (i - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1
                # Note: max_freq recalculation and window shrinking could be
                # optimized away — max_freq never needs to decrease since
                # we only care about beating the current best window size.
                max_freq = max(count.values())

            print(s[start: i + 1])

            # Keep track of max_size reached.
            max_size = max(max_size, i - start + 1)

        return max_size

    def characterReplacement_Efficient(self, s: str, k: int) -> int:
        # Algorithmic idea:
        # Slide a window across s
        # and only increase it when we have found
        # a window that allows it.
        max_freq: int = 0
        count: dict[str, int] = {}
        start: int = 0

        # Invariant: current window size is the larget valid
        # one we have found and we only increase it when we
        # find another one that allows said increase in size.
        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            # Meta invariant:
            # Hashmap (or data structure in use)
            # must mimmic the current state of the window.
            if (i - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1
        return i - start + 1


sol = Solution()
print(sol.characterReplacement_Efficient('BAACDEFFFAACC', 2))
