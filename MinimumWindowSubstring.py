class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Algorithmic idea:
        # Grow a window until it contains the required chars in t.
        # Then, shrink it as much as possible while recording
        # the min len achieved.
        # After that, the window will be invalid so we grow it again
        # until it is again complete.
        # Repeat process until we go through the entirety of s.
        if not t:
            return ''
        t_count, window = {}, {}
        l: int = 0
        min_len: int = float('inf')
        min_window: tuple[int, int] = (-1, -1)

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        # Note:
        # We can avoid dict comparision, which would be O(k)
        # with the implementation of variables that track how many
        # char requirements are needed (need), and how many we have (have).
        have, need = 0, len(t_count)
        # Invariant:
        # Grow window while requirements aren't being met.
        # Shrink while they are.
        for i, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in t_count and t_count[c] == window[c]:
                have += 1

            while have == need:
                if i - l + 1 < min_len:
                    min_window = l, i + 1
                    min_len = i - l + 1

                window[s[l]] -= 1

                if (s[l] in t_count
                        and window[s[l]] < t_count[s[l]]):
                    have -= 1
                l += 1
        l, r = min_window
        return s[l: r] if min_len != float('inf') else ''


sol = Solution()
print(sol.minWindow("AACABA", 'ABA'))
