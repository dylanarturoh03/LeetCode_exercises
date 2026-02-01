class Solution:
    def containerWithMostWater(self, heights: list[int]) -> int:
        maxCapacity: int = 0
        L: int = 0
        R: int = len(heights) - 1
        
        while L < R:
            height: int = min(heights[L], heights[R])
            width: int = R - L
            capacity: int = width * height
            
            if capacity > maxCapacity:
                maxCapacity = capacity
            
            if height == heights[L]:
                L += 1
            else:
                R -= 1
        
        return maxCapacity


sol = Solution()
print(sol.containerWithMostWater([1,7,2,5,4,7,3,6]))
                   