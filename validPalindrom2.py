class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(curr_l: int, curr_r: int) -> bool:
            '''
            Return True if the substring s[curr_l:curr_r+1] is a palindrome.
            '''
            while curr_l < curr_r:
                if s[curr_l] != s[curr_r]:
                    return False

                curr_l += 1
                curr_r -= 1

            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return helper(l, r - 1) or helper(l + 1, r)

            l += 1
            r -= 1

        return True


sol = Solution()
print(sol.validPalindrome('abbda'))
