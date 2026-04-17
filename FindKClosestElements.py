class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Algorithmic Idea:
        # Slide a window size k through arr.
        # The objective is to find the best start possible
        # for our window based on proximity of num to x
        # and, since we have a preference towards smaller values,
        # then we only set a later window as the best start if
        # it is stricly better than what currently is recorded.
        left: int = 0
        best_start: int = 0
        # Invariant:
        # Best start is the best possible earliest window.
        # We only update if something better was found.
        for i in range(k, len(arr)):
            a: int = arr[left]
            b: int = arr[i]
            diff_a: int = abs(a - x)
            diff_b: int = abs(b - x)

            left += 1  # Increment left so best_start matches a + 1 pos.

            if diff_b < diff_a:
                best_start = left
        # Due to the fixed nature of this problem,
        # we slice the best window by only knowing it's start.
        return arr[best_start: best_start + k]


sol = Solution()
print(sol.findClosestElements([2, 3, 4], 1, 3))
