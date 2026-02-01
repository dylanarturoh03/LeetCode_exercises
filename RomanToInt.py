class Solution:
    symbols = {'I' : 1,            
               'V' : 5,
               'X' : 10,            
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000,
               'IV' : 4,
               'IX' : 9,
               'XL' : 40,
               'XC' : 90,
               'CD' : 400,
               'CM' : 900}
    
    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0


        while i < len(s) :
            
            if i == len(s) -1:
                count += self.symbols.get(s[i])
                i+=1
            else :

                if s[i] + s[i+1] in self.symbols:
                    count += self.symbols.get(s[i] + s[i+1])
                    i+=2

                else:
                    count += self.symbols.get(s[i])
                    i+=1

        return count
    


sol = Solution()
print(sol.romanToInt('MCMXCIV'))