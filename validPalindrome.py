class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedStr = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(processedStr)-1

        while right > left:
            
            if processedStr[left] != processedStr[right]:
                return False
            
            left+=1
            right-=1


        return True
    
sol = Solution()
print(sol.isPalindrome('Was it a car or a cat I saw?'))