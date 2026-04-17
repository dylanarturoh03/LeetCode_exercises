class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        def isCollision(a: int, b: int):
            return a > 0 and b < 0

        stack: list[int] = []
        for ast in asteroids:
            while stack and isCollision(stack[-1], ast):
                if stack[-1] > abs(ast):
                    ast = 0
                    break
                elif stack[-1] == abs(ast):
                    ast = 0
                    stack.pop()
                    break
                else:
                    stack.pop()

            if ast:
                stack.append(ast)
        return stack


sol = Solution()
print(sol.asteroidCollision([7, 1, -6]))
