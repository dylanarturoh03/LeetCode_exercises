class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not t:
            return 0

        pointerT: int = 0
        pointerS: int = 0

        while pointerS < len(s):
            if s[pointerS] == t[pointerT]:
                pointerT += 1

                if pointerT == len(t):
                    return 0

            pointerS += 1

        return len(t) - pointerT


sol = Solution()
print(sol.appendCharacters('coaching', 'coding'))
