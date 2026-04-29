class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        days: int = -1  # Initialize in -1 to cover impossible case
        lo, hi = 1, max(bloomDay)
        # Algorithmic idea:
        # Since we are looking to minimize the days
        # needed to create m bouquets, then our search space
        # will be the number of days, in which the smallest reasonable
        # day is 1 (lo) because it means we can collect all flowers in day 1,
        # and the highest is the max bloomDay (hi) because it is
        # the first confirmed day where we can collect all flowers.
        while lo <= hi:
            midDay: int = (hi + lo) // 2
            # For every day we try
            # we go throught the garden grabbing
            # flowers that have already bloomed
            # and if the number of consecutive valid flowers
            # reaches K we can form a bouquet.
            # After that we reset the number of flowers and continue
            # the garden tour.
            n_bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom <= midDay:
                    flowers += 1

                    if flowers == k:
                        n_bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            # If number of bouquets formed is greater or equal than m
            # it means we can satisfy the bouquets condition
            # thus, this is the lowest valid answer so far.
            if n_bouquets >= m:
                days = midDay
                # Shrink search space leftward to find
                # an even smaller valid day
                hi = midDay - 1
            else:
                # Else, if n_bouquets can't satisfy condition m
                # we shrink search space rightward, because
                # every day before midDay also won't be able to do so.
                lo = midDay + 1
        return days  # Return minimized n_days to satisfy m


sol = Solution()
print(sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
