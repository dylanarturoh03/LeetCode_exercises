class solution:
    def isPalindromeVerbose(self, x: int) -> bool:
        xstr = str(x)
        ogWord = []
        reversedWord = []

        for w in xstr:
            ogWord.append(w)

        for w in reversed(xstr):
            reversedWord.append(w)

        if ogWord == reversedWord:
            return True

        return False
    
    # Less redudant / verbose version:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        #print(list(xstr))
        #print(list(reversed(xstr)))
        #return list(xstr) == list(reversed(xstr)) es redundante crear a listas a base de strings
        return xstr == xstr[::-1]

        
    
sol = solution()
print(sol.isPalindromeVerbose(-121))
print(sol.isPalindrome(-121))