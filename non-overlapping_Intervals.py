class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Algorithmic idea:
        # Get rid of overlaps in the least amount of deletions possible.
        # Analyze intervals, if there is an overlap we count it and keep
        # the interval that has the shortest reach,
        # since it has less likelyhood of causing more overlaps.
        overlap_intervals: int = 0
        intervals.sort()

        segment_end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval_start, interval_end = intervals[i]

            if interval_start < segment_end:
                # Greedy choice:
                # When an overlap is found, it is important
                # to keep the interval with the shortest reach,
                # since it has less chances of causing another one.
                overlap_intervals += 1

                # We are only keeping track of end and not start, because
                # only the end will allow us to detect overlaps and choose
                # the most convenient interval, so to speak.
                segment_end = min(segment_end, interval_end)
            else:
                segment_end = interval_end

        return overlap_intervals


sol = Solution()
print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [2, 2]]))
