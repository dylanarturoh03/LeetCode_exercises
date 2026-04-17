class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        c: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num in c and abs(c[num] - i) <= k:
                return True

            c[num] = i
        return False

    def CND_Window(self, nums: list[int], k: int) -> bool:
        # Algorithmic Idea:
        # The objective is to find two duplicates whose positions
        # abs(i - j) <= k.
        # In order to achieve that a window of valid elements is created
        # and if we ever find a duplicate within that window it means
        # a the objective has been achieved.
        # Valid elements are the ones whose positions diff are
        # within contraint.
        window: set[int] = set()

        # Invariant:
        # All the values within window are valid candidates

        # Fill and update window whenever it gets too long
        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])

        return False


sol = Solution()
print(sol.CND_Window([1, 2, 3, 4, 2, 2], 2))
