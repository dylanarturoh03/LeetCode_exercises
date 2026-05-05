class Solution:
    def reverseInt(self, x: int) -> int:
        # Algorithmic idea:
        # Get the last integer from x into reversed_x
        # then perform integer division to reduce the last digit of x.
        # Continue until x == 0.

        # Key insight:
        # Python integer division truncates towards negatives, not 0.
        # This means when doing floor division on an negative number
        # we will actually go further from 0 rather than towards it.
        # This is why we work with abs(x) and re-add the symbol later
        # instead of working directly with x.

        # Example:

        # Float division
        # 12 / 10 = 1.2
        # -12 / 10 = -1.2

        # Integer divison
        # 12 // 10 = 1
        # -12 // 10 = -2
        symbol: int = -1 if x < 0 else 1
        x = abs(x)
        reversed_x: int = 0
        while x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        reversed_x *= symbol
        return reversed_x if -2 ** 31 <= reversed_x <= 2 ** 31 - 1 else 0 


sol = Solution()
print(sol.reverseInt(123))