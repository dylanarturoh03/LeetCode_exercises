class Solution:
    def isValidWordSquare(self, words: list[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                # Check if row J exists in the list
                if j >= len(words):
                    return False
                # Check if col i exists in row j
                if i >= len(words[j]):
                    return False
                # Check if the current position points to
                # the same value as row j, col i
                if words[i][j] != words[j][i]:
                    return False
        return True


sol = Solution()
print(sol.isValidWordSquare(["abc",
                            "bnr",
                             'cr']))
