class Solution:
    def trap(self, heights: list[int]) -> int:
        stack: list[int] = []
        water: int = 0
        # Invariant
        # We are looking for left and right boundaries at every index.
        # In order to achieve O(n) a monotonic stack is used.
        # Every element in the stack is waiting for a right boundary.
        # Left boundary is the element below it. If no element is below,
        # it means no boundary is there, thus, no water.
        # The decreasing (top - bottom) stack guarantees that the floor is
        # never bigger than a boundary.

        # Something I noticed, is that this monotonic property
        # guarantees that inner pockets are resolved first,
        # which evens the floor with water, so that outer pockets can make
        # use of this even property for their calculations.
        for n in range(len(heights)):
            while stack and heights[stack[-1]] < heights[n]:
                floor: int = heights[stack.pop()]
                if stack:
                    l: int = stack[-1]
                    water += (((min(heights[l], heights[n]))
                              - floor) * (n - l - 1))
            stack.append(n)
        return water


sol = Solution()
print(sol.trap([2, 1, 0, 1, 3]))
