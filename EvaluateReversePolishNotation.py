from typing import Callable, TypeAlias
import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        opFunc: TypeAlias = Callable[[int, int], int]
        ops: dict[str, opFunc] = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        # Algorithmic idea:
        # Create a stack that and store values to help simulate RPN
        # The core idea is with RPN is number, number, operand...
        # So at all times the topof stack must have the most recent numbers,
        # which will be popped when used for an operation.
        # The end result of the operation will be the only remaining thing
        # in stack.
        stack: list[int] = []
        # Invariant:
        # the two elements at the top of stack are always
        # the most recent operands.
        for token in tokens:
            if token in ops:
                b: int = stack.pop()
                a: int = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[-1]


sol = Solution()
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
