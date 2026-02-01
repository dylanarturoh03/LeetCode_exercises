class Solution:

    symbols = {'I' : 1,
               'V' : 5,
               'X' : 10,
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000}

    def romanToInt(self, s: str) -> int:
        count = self.symbols.get(s[0])

        for i in range(1, len(s)):
            
            if self.symbols.get(s[i]) > self.symbols.get(s[i-1]):
                count += self.symbols.get(s[i]) - self.symbols.get(s[i-1]) * 2
            else:
                count += self.symbols.get(s[i])

        return count
    

sol = Solution()
print(sol.romanToInt('MXLVIII'))