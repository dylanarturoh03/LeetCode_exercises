class solution:
    def isPalindrome(self, x: int) -> bool:
        # Filter inputs
        # Move the first half of a nomber into a diferent var
        # Reverse it

        if (x < 0 or( x % 10 == 0 and x!=0)):
            return False


        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x%10
            x = x//10
            


        return x == reversed_half or x == reversed_half // 10
    



sol = solution()
print(sol.isPalindrome(0))