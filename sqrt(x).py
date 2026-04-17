class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x if x < 4 else x // 2
        # Invariant:
        # When x has an exact sqrt we return mid.
        # When it does not, no exact match will be found.
        # Thus, causing the pointers to eventually cross.
        # When this happens, we know the exact sqrt is between
        # high and low, but since we can't represent it, we must round down.
        # In this case, the pointers are guaranteed to be low > high.
        # When this happens, high is the largest integer whose square is still
        # less than x, and low is the smallest whose square exceeds x.
        # Since we need the floor, we return high.
        while low <= high:
            mid: int = (high + low) // 2
            square: int = mid ** 2
            if square < x:
                low = mid + 1
            elif square > x:
                high = mid - 1
            else:
                return mid
        return high

    def mySqrt_NewtonM(self, x: int) -> int:
        r: int = x
        while r * r > x:
            r = (r + x // r) >> 1
        return r


sol = Solution()
print(sol.mySqrt_NewtonM(13))
