class Solution:
    def containerWithMostWater(self, heights: list[int]) -> int:
        maxCapacity: int = 0
        
        for bar in range(len(heights) - 1):
            L: int = bar
            R: int = len(heights) - 1
            
            while L < R:
                auxCap: int = 0
                width: int = R - L
                
                if heights[L] > heights[R]:
                    lowerBar: int = heights[R]
                else:
                    lowerBar: int = heights[L]
                
                auxCap = lowerBar * width
                
                if auxCap > maxCapacity:
                    maxCapacity = auxCap
                
                R -= 1
                
        return maxCapacity


sol = Solution()
print(sol.containerWithMostWater([1,7,2,5,4,7,3,6]))