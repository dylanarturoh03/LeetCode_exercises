class Solution:
    def dialyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Algorithmic idea:
        # Use monoronic stack containing (temp[i], i)
        # so that at every point we can easily compute
        # how many days have passed since nge and current i.
        ng: list[int] = [0] * len(temperatures)
        monotonicStack: list[tuple[int, int]] = []
        # Invariant:
        # Top of the stack is always the current nge.
        for i in range(len(temperatures) - 1, -1, -1):
            # Pop all smaller or equal temperatures: they cannot be
            # next greater for current or any left element
            while monotonicStack and monotonicStack[-1][0] <= temperatures[i]:
                monotonicStack.pop()

            if monotonicStack:
                # The top of the stack is the next warmer day;
                # compute how many days away
                ng[i] = monotonicStack[-1][1] - i

            monotonicStack.append((temperatures[i], i))
        return ng


sol = Solution()
print(sol.dialyTemperatures([30, 38, 30, 36, 35, 40, 28]))
