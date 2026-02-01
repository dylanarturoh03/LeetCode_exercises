class Solution:
    def isValidAnagram(self, s: str, t:str) -> bool:
        return sorted(s) == sorted(t)
    
sol = Solution()
print(sol.isValidAnagram('racecar', 'carrace'))