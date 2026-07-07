class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if not carry:
                return digits
            res = digits[i] + carry
            digit = res % 10
            carry = res // 10
            digits[i] = digit
        if carry:
            digits.insert(0, carry)
        return digits


sol = Solution()
print(sol.plusOne([9, 9, 9]))
