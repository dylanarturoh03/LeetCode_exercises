from typing import List

class Solution:
    def commonPrefix(self, strs: List[str]) -> str:
        cf=''
        cutWords=[]

        # 1 - Check if there are any empty strings 
        if '' in strs:
            return ''
        
        # 2 - Cut every word to the length of the smallest string
        smallest = len(min(strs, key=len))
        
        for i in range(0, len(strs)):
            cutWord=''

            for j in range(0, smallest):
                cutWord+= strs[i][j]
           
            cutWords.append(cutWord)

        # 3 - Compare positions and add characters to prefix bar until prefix is broken

        print(cutWords[0][1])
        print(cutWords[1][1])
        print(cutWords[2][1])
        print(cutWords[0][2])
        print(cutWords[1][2])
        print(cutWords[2][2])

        numberWords = 


        return cf
    
sol = Solution()
print(sol.commonPrefix(['flow', 'flower', 'flight']))