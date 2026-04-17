from random import randint


class Solution:
    def __init__(self, n: int):
        self.n = n
        self.pick = randint(1, n)

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

    def guessNumber(self) -> int:
        low, high = 1, self.n

        while True:
            mid: int = (high + low) // 2
            g: int = self.guess(mid)
            if g < 0:
                high = mid - 1
            elif g > 0:
                low = mid + 1
            else:
                return mid


sol = Solution(10)
print(sol.guessNumber())
