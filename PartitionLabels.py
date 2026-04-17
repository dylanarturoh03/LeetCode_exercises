class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        if not s:
            return []
        # Algorithmic ideas:
        # We are first define position intervals for each letter
        # Then we go through them and merge them if they overlap.
        # If we find a segment that does not, then we compute the length
        # of the current segment and append it to the partitions list.
        letter_intervals: list[list[int]] = []
        seen: dict[str, int] = {}
        partitions: list[int] = []

        # Define intervals and order them by birth
        for i, char in enumerate(s):
            if char not in seen:
                # Create interval
                seen[char] = len(letter_intervals)
                letter_intervals.append([i, i])
            else:
                # Update death of interval
                letter_intervals[seen[char]][1] = i

        # Merge intervals
        segment_start, segment_end = letter_intervals[0]
        for interval in range(1, len(letter_intervals)):
            interval_start, interval_end = letter_intervals[interval]
            # Greedy idea:
            # Merge intervals while they overlap
            # Once they do not,
            # then we move on to building the next segment.
            # We construct segments by keeping track of two pointers
            # one at the start of the new segment (segment_start)
            # and the other one at the end (segment_end)
            if interval_start <= segment_end:
                segment_end = max(interval_end, segment_end)
            elif segment_end < interval_start:
                # partition: int = segment_end - segment_start + 1
                partitions.append([segment_start, segment_end])
                segment_start, segment_end = interval_start, interval_end
        partitions.append([segment_start, segment_end])
        return partitions

    def partitionLabels_Optimal(self, s: str) -> list[int]:
        # Algorithmic idea:
        # Go through the array until we reach the end boundary.
        # The end boundary is dictated by the last occurence of every char.
        # So, in order to count partitions you have to keep going until
        # every char's end condition within the segment has been satisfied.
        partitions: list[int] = []
        last_pos: dict[str: int] = {char: i for i, char in enumerate(s)}

        size: int = 0
        end: int = 0

        for i, char in enumerate(s):
            end = max(end, last_pos[char])
            size += 1
            # Greedy choice:
            # The moment i reaches the end, we cut the segment
            # because all of the internal characters have met their end.
            if i == end:
                partitions.append(size)
                size = 0

        return partitions


sol = Solution()
print(sol.partitionLabels("llñpppjfnsawecjhh"))
