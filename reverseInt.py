def reversedInt(n: int) -> int:
    sign: int = -1 if n < 0 else 1
    reversedInt: int = 0
    n = abs(n)

    while n != 0:
        reversedInt = reversedInt * 10 + (n % 10)
        n = n // 10

    return reversedInt * sign


print(reversedInt(-123))
