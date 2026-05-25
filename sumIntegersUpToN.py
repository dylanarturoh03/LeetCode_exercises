def sum(n: int) -> int:
    if not n:
        return n
    else:
        return n + sum(n - 1)


def fibonacci(n: int) -> int:
    '''Naive fibonacci function. Time complexity: O(2^n)'''
    # BASE CASE
    if n == 0:
        return 0
    if n == 1:
        return 1

    # RECURSIVE CASE
    return fibonacci(n - 1) + fibonacci(n - 2)


def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[1:-1]) + s[0]


print(reverse('racecar'))
