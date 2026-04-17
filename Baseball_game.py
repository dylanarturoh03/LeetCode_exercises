class Solution:
    def calPoints(self, operations: list[str]) -> int:
        def is_valid_integer(s: str):
            try:
                int(s)
                return True
            except ValueError:
                return False

        stack_records: list[int] = []
        points: int = 0

        for op in operations:
            match op:
                case str() if is_valid_integer(op):
                    n = int(op)
                    stack_records.append(n)
                    points += n
                case '+':
                    n = stack_records[-1] + stack_records[-2]
                    stack_records.append(n)
                    points += n
                case 'D':
                    n = stack_records[-1] * 2
                    stack_records.append(n)
                    points += n
                case 'C':
                    points -= stack_records.pop()
        return points


sol = Solution()
print(sol.calPoints(['1', '2', '+', 'C', '5', 'D']))
