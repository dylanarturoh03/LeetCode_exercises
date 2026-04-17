class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i: int = 0  # Greed pointer
        j: int = 0  # Cookie pointer

        # We sort them to greedily match
        # the smallest cookie with the least greedy child
        g.sort()
        s.sort()

        while i < len(g) and j < len(s):
            # If current cookie is able to satisfy the current child's greed
            # we give it to it and move on to the next kid.
            if s[j] >= g[i]:
                i += 1

            # Otherwise, we discard the current cookie anyways.
            # This is it because it means the cookie won´t be able to
            # calm any further infant due to them having the same
            # or higher greed factor.
            j += 1

        return i


sol = Solution()
print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
