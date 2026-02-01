
class solution:
    def isPalindrome(self, x: int) -> bool:
        # Filter inputs
        # Move the first half of a nomber into a diferent var
        # Reverse it

        if (x < 0 or( x % 10 == 0 and x!=0)):
            return False


        reversed_half = 0
        aux_x = 0
        aux_rh = 0

        if(x != 0):
            while x > reversed_half:
                reversed_half = reversed_half * 10 + x%10
                x = x//10
            
            aux_x = x
            aux_rh = reversed_half

            while aux_x > 0:
                aux_x = aux_x // 10
                aux_rh = aux_rh // 10


            if aux_rh != 0:
                reversed_half = reversed_half // 10


        return x == reversed_half
    



sol = solution()
print(sol.isPalindrome(9995999))