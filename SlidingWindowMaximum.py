from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_nums: list[int] = []
        window: dict[int, int] = {}
        l: int = 0

        for i, n in enumerate(nums):
            window[n] = window.get(n, 0) + 1

            if i - l + 1 == k:
                max_nums.append(max(window.keys()))

            if i - l + 1 > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                max_nums.append(max(window.keys()))
                l += 1
        return max_nums

    def maxSlidingWindow_logicalinvalid(self, nums: list[int], k: int) -> list[int]:
        max_nums: list[int] = []
        window: dict[int, int] = {}

        for i, n in enumerate(nums):
            window[n] = i

            if i >= k - 1:
                max_nums.append(max(key for key, v in window.items() if v > i - k))
        return max_nums

    def maxSlidingWindow_optimal(self, nums: list[int], k: int) -> list[int]:
        '''Monotonic idea: Discard elements that can never be the answer.'''
        # Algorithmic idea:
        # Make use of a monotonic deque to guarantee easy access
        # to max element at every window.
        output: list[int] = []
        q: deque[int] = deque()
        l = r = 0

        # Invariant:
        # q[0] is always the max at current window.
        while r < len(nums):
            # Pop all previous elements if a new max was found.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # Pop out of bounds elements.
            if l > q[0]:
                q.popleft()
            # Slide window
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


sol = Solution()
print(sol.maxSlidingWindow_optimal([1, 2, 1, 0, 4, 2, 6], 3))
