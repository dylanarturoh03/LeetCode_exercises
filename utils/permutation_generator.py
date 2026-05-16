from random import getrandbits
from math_utils import isCoprime


def gen_permutatition(a: int, b: int) -> None:
    if a > b:
        a, b = b, a

    x: int = getrandbits(256)
    n: int = b - a + 1
    while not isCoprime(n, x):
        x = getrandbits(256)

    c: int = getrandbits(256)

    for i in range(n):
        print((x * i + c) % n + a, end=" -> ")
    print("None")


gen_permutatition(5, 9)
