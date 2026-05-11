class Solution:
    '''
        Every natural number is either happy or not. Happy numbers form
        infinitely many paths which eventually converge at 1.
        Unhappy ones do the same, but instead they arrive at the unhappy cycle:
        4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4, from which they will
        never get out.
    '''
    UNHAPPY_CYCLE: set[int] = {4, 16, 37, 58, 89, 145, 42, 20}

    def _sqrsDigits(self, n: int) -> int:
        '''Compute the sum of squares of n's digits.'''
        res: int = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        '''Determine if a number is happy using Floyd's algorithm.'''
        slow = fast = n
        # Algorithmic idea:
        # Floyd's algorithm states that if there is a cycle, two pointers
        # will eventually hit each other if they go at different speeds.

        # Applied to this problem, slow and fast are going through a
        # deterministic chain of numbers which eventually converges at 1
        # or cycles through itself forever without ever hitting 1.

        # If our pointers are eventually positioned at the same number,
        # inspite of fast going twice as fast a slow, it means there is a cycle
        # and this number will never hit 1. Else, it means fast hits 1
        # and the number is considered happy.
        while True:
            slow = self._sqrsDigits(slow)
            fast = self._sqrsDigits(self._sqrsDigits(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False

    def isHappy_Hash(self, n: int) -> bool:
        '''Determine if a number is happy using a hash set.'''
        results: set[int] = set()
        # Algorithmic idea:
        # Unlike floyd's implementation, here we just save
        # values and if we ever see them again it means it is
        # a cycle, otherwise we just hit 1 and end the loop.
        while n != 1:
            if n in results:
                return False

            results.add(n)
            n = self._sqrsDigits(n)
        return True

    def isHappy_Hardcoded(self, n: int) -> bool:
        '''Determine if a number is happy using domain knowledge.'''
        # Algorithmic idea:
        # Since we know a number eventually converges to 1 or one of
        # the elements in the unhappy cycle, then just follow the path
        # from n until it reaches one of these points.

        # If by the end n is not 1, then it means it hit the unhappy cycle
        # and it will never escape it.
        while n not in self.UNHAPPY_CYCLE and n != 1:
            n = self._sqrsDigits(n)
        return n == 1


sol = Solution()
print(sol.isHappy_Hash(19))
