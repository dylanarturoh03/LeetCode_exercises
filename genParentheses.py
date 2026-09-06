class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        '''Recursively build all valid parenthesis strings.'''
        path, res = [], []

        def backtrack(openers: int = 0, closers: int = 0) -> None:
            # Base case
            if len(path) == n * 2:
                res.append(''.join(path))
                return

            # Add opener case
            if openers < n:
                path.append('(')
                backtrack(openers + 1, closers)
                path.pop()

            # Add closer case
            if openers > closers:
                path.append(')')
                backtrack(openers, closers + 1)
                path.pop()

        backtrack()
        return res


sol = Solution()
print(sol.generateParenthesis(2))
