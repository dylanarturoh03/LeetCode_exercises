class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = ('#').join(s.split())
        lastWord: int = 0

        for char in s:
            lastWord += 1

            if char == '#':
                lastWord = 0

        return lastWord

    def lengthOfLastWordReverse(self, s: str) -> int:
        lastWord: int = 0
        for char in range(len(s) - 1, -1, -1):
            if s[char].isalnum():
                lastWord += 1

                if not s[char - 1].isalnum():
                    break

        return lastWord


sol = Solution()
print(sol.lengthOfLastWordReverse('World'))
