class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives: int = 0
        tens: int = 0

        for bill in bills:

            match bill:
                case 5:
                    fives += 1
                case 10:
                    if fives == 0:
                        return False

                    fives -= 1
                    tens += 1
                case 20:
                    if tens > 0 and fives > 0:
                        fives -= 1
                        tens -= 1
                    elif fives >= 3:
                        fives -= 3
                    else:
                        return False

        return True


sol = Solution()
print(sol.lemonadeChange([10]))
