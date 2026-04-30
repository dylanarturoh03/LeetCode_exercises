class Solution:
    def aggressiveCows(self, stalls: list[int], k: int) -> int:
        # Algorithmic idea:
        # Binary search on the answer + greedy validation check
        # Since we want to find the maximum minimum distance
        # then search space becomes the answer itself.

        # lo is the minimum distance there could be. Since
        # stall positions are always unique, then the least d
        # possible is 1.

        # hi is the maximum distance possible with this array.
        # The problem requires sorting for both efficient search
        # space definition, and greedy validation check.
        # In this case the max min distance is the difference between
        # the last and first stall (sorted by stalls[i])
        stalls.sort()
        lo, hi = 1, stalls[-1] - stalls[0]
        minDistance: int = lo

        while lo <= hi:
            mid: int = (hi + lo) // 2
            # This is the greedy validation check.
            # For every candidate distance we must check
            # if it is possible to greedily place all cows
            # with distance >= mid from one another.
            cows, distance = k - 1, 0
            # For each tour around the farm a cow is placed
            # in the first stall, and then try to place
            # k - 1 cows in remaining stalls.
            # A cummulative sum of distance is kept until d >= mid.
            # At that point we place the cow
            # at current stall and the sum is reset.
            for i in range(1, len(stalls)):
                dif: int = stalls[i] - stalls[i - 1]
                if distance + dif >= mid:
                    distance = 0
                    cows -= 1
                else:
                    distance += dif

            # If cows remain, which means it was not possible to place
            # all cows in the given stalls with a difference of mid from
            # one another.
            if cows > 0:
                # Search space is reduced leftward, because
                # every distance after mid will also not work.
                hi = mid - 1
            else:
                # If cows do not remain, it means it was possible to do so.
                # A possible candidate has been found.
                # Then, shrink rightwards to look for larger valid distances.
                minDistance = mid
                lo = mid + 1
        return minDistance


sol = Solution()
print(sol.aggresiveCows([10, 1, 2, 7, 5], 3))
