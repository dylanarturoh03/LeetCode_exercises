class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''Add two given string represented binary numbers.'''
        # Ensure a is always the longer string.
        if len(b) > len(a):
            a, b = b, a

        diff, carry = len(a) - len(b), 0
        res = []

        # Iterate backwards through the longer string
        for i in range(len(a) - 1, -1, -1):
            # Calculate the matching index for b, the shorter string
            j = i - diff

            # Get corresponding char for both strings
            dA = int(a[i])
            # If b goes negative it means it's been exhausted,
            # so pad out with 0's
            dB = int(b[j]) if j >= 0 else 0

            # Compute binary representation of total
            total = dA + dB + carry
            res.append(str(total % 2))
            carry = total // 2

        # Append carry in case some still remained
        if carry:
            res.append(str(carry))

        # Reverse the array because of the backwards logic of the algorithm
        res.reverse()
        return ''.join(res)


sol = Solution()
print(sol.addBinary('10', '1'))
