from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        k: int = high
        # Invariant:
        # Everything below low is insuficcient to reach h.
        # Everything above high is sufficient but no minimal.
        # Everything in between is untested.
        while low <= high:
            mid: int = (high + low) >> 1
            k_hours: int = sum(ceil(pile / mid) for pile in piles)

            if k_hours > h:
                low = mid + 1
            else:
                k = mid
                high = mid - 1
        return k


sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))
