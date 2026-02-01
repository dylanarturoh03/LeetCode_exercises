def reverseString(s: list[str]) -> None:
    L: int = 0
    R: int = len(s) - 1
    
    while L < R:
        aux: str = s[L]
        s[L] = s[R]
        s[R] = aux
        L += 1
        R -= 1

    print(s)


defaultString: list[str] = ["n", "e", "e", "t"]
print(reverseString(defaultString))
