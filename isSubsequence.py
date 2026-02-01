class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        pointerS: int = 0
        pointerT: int = 0

        while pointerT < len(t):
            if t[pointerT] == s[pointerS]:
                pointerS += 1

                if pointerS == len(s):
                    return True

            pointerT += 1

        return False


sol = Solution()
print(sol.isSubsequence('hellooo', 'hbbealalaooao'))
