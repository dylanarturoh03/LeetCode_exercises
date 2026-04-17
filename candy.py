from itertools import pairwise


class Solution:
    def candy_greedy(self, ratings: list[int]) -> int:
        candies: list[int] = [1 for _ in ratings]

        for i in range(1, len(candies)):

            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for j in range(len(candies) - 2, -1, -1):

            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)

        return sum(candies)

    def candy_one_pass(self, ratings: list[int]) -> int:
        # Algorithmic idea:
        # Candy is at it's core a geometric problem.
        # One we can visualize when we draw ratings as (x, y) coordinates.
        # Now... the candy distribution follows that structure
        # So, we can build slopes or triangles (both upward & downward)
        # and count the height of it at the current point
        # following the problems contraints.

        # Invariant:
        # Slopes are always (1, 2, 3, 4...)
        # unless the merging requires differently.
        # And, the scope is local at every sub-problem.

        # Candy count is initialized at 1 because of constraints
        candies: int = 1
        # Consecutive number of upward steps
        up: int = 0
        # Consecutive number of downward steps
        down: int = 0
        # Current local peak to ensure correct merging.
        max_height: int = 0

        # Greedy idea:
        # Add candies at every step based on slope progression.
        # It is worht noting, that this one pass version is more of
        # mathematical solution...
        # So it isn't really a classic greedy algorithm.
        for prev, curr in pairwise(ratings):
            # Case when we take an upward step
            if curr > prev:
                down = 0  # Reset downwards step
                up += 1  # Add upward step
                max_height = up + 1  # Update local max height
                candies += 1 + up  # Add the height at current point

            # Case when downward step is taken
            elif curr < prev:
                up = 0  # Reset upwards steps.
                down += 1  # Add downward step.

                # Adjust merging at max_peak when right slope is longer
                if max_height <= down:
                    candies += 1  # Add additional candy to max_peak
                candies += down  # Add height at current point

            # Case when flat
            else:
                # Due to problem's constraints we reset the subproblem
                up = 0
                down = 0
                max_height = 0
                candies += 1
        return candies


sol = Solution()
print(sol.candy_one_pass([4, 3, 5]))
