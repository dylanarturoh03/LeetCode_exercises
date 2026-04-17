from math import ceil


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        total, max_weight = 0, 0
        for w in weights:
            total += w
            max_weight = max(max_weight, w)

        low = max_weight
        # Upper bound is decided based on min of:
        # sum(weights): The capacity needed if we had to do it in a day.
        # ceil(w.len / d) * max(w) = Upper bound based on worst case.
        # We calculate the packages per day we would have to load
        # in order to make it in time, but assume all weights are equal
        # to the max(w) in order to have the worst possible case.
        high = min(total, ceil(len(weights) / days) * max_weight)
        min_capacity = high

        while low <= high:
            mid: int = (high + low) >> 1
            mid_days, curr_w = 1, 0
            for w in weights:
                if curr_w + w <= mid:
                    curr_w += w
                else:
                    mid_days += 1
                    curr_w = w
            # Invariant:
            # We greedily calculate the min number of days it takes to load
            # all packages with mid capacity as a max.
            # If mid_days > days: We can't possibly do it in n days,
            # so all candidates below it are discarded because they are worse
            # than current, which already doesn't work.
            # if mid_days <= days: We have found a candidate, so it is saved
            # in min_capacity. Now reduce search space for all valid candidates
            # below it because a better candidate could be found.
            if mid_days > days:
                low = mid + 1
            else:
                min_capacity = mid
                high = mid - 1
        return min_capacity


sol = Solution()
print(sol.shipWithinDays([2, 4, 6, 1, 3, 10], 4))
