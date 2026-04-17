class Solution:
    def largestRectangleArea_bruteForce(self, heights: list[int]) -> int:
        max_area: int = 0

        for i, h in enumerate(heights):
            # First idx to the left that is shorter than h.
            j = i - 1
            while j >= 0 and heights[j] >= h:
                j -= 1
            # First idx to the right that is shorter than or equal to h.
            k = i + 1
            while k < len(heights) and heights[k] > h:
                k += 1

            max_area = max(max_area, h * (k - j - 1))
        return max_area

    def largestRectangleArea_MStack(self, heights: list[int]) -> int:
        heights.append(-1)
        stack: list[int] = []
        max_area: int = 0
        # Invariant:
        # Every element in stack has yet to found it's
        # right boundary.
        # Left boundary is below each element. If element has nothing
        # below, it means the left boudary is the beginning of array.
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h: int = heights[stack.pop()]
                l: int = stack[-1] if stack else -1
                max_area = max(h * (i - l - 1), max_area)
            stack.append(i)
        return max_area


sol = Solution()
print(sol.largestRectangleArea_MStack([1, 1, 1, 1, 13, 1, 1, 5, 6]))
