def gcd(a: int, b: int) -> int:
    '''Recursive Euclid's algorithm to get the GCD of a and b'''
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


def isCoprime(a: int, b: int) -> int:
    '''Determine if a and b are coprimes.'''
    # A number is a coprime of another if their greatest common divisor is 1.
    return gcd(a, b) == 1


if __name__ == '__main__':
    print(gcd(5, 10))
    print(gcd(1260, 1890))
    print(gcd(1260 - 1890, 1890))
