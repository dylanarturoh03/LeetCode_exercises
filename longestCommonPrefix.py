class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''

        longest_prefix: list[int] = []
        shortest = len(min(strs, key=len))
        for i in range(shortest):
            first: str = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != first:
                    return ''.join(longest_prefix)

            longest_prefix.append(first)

        return ''.join(longest_prefix)


sol = Solution()
print(sol.longestCommonPrefix(["bat", "bag", "bank", "band"]))
