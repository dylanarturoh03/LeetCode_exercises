class Solution:
    def isValid(self, s: str) -> bool:
        # Algorithmic idea:
        # Track if every opening bracket closes in the correct
        # order.
        # Push when opening a bracket.
        # Pop when closing it, but before closing correct order must
        # be ensured, otherwise it isn't valid.
        def closing_bracket(c: str) -> str:
            match c:
                case ')': return '('
                case ']': return '['
                case '}': return '{'
        # Stack is the perfect data structure
        # since we are asked to close the brackets in reversed
        # order.

        # Example: {([])}
        # 1 - Open {
        # 2 - Open (
        # 3 - Open [

        # 4 - Close ]
        # 5 - Close )
        # 6 - Close }

        # As you can see, the closing order perfectly follows
        # LIFO because the most recent brackets must be closed first.
        stack: list[str] = []
        # Invariant:
        # Every element in the stack is yet to be closed.
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in '}])':
                if not stack or stack[-1] != closing_bracket(c):
                    return False
                stack.pop()
        return not stack


sol = Solution()
print(sol.isValid('2{([])}3'))
