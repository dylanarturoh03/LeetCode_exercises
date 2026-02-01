class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water: int = 0

        while l < r:
            # We work with the pointer whose side has the lower max wall
            if max_l <= max_r:
                # 1 - Move pointer inward
                l += 1
                # 2 - Define the bigger wall to the left
                max_l = max(max_l, height[l])
                # 3 - Calculate how much water sits on that bar
                water += max_l - height[l]
            else:
                # 1 - Move pointer inward
                r -= 1
                # 2 - Define the bigger wall to the right
                max_r = max(max_r, height[r])
                # 3 - Calculate how much water sits on that bar
                water += max_r - height[r]

        return water


sol = Solution()
print(sol.trap([349, 199, 200, 9, 104, 259]))
