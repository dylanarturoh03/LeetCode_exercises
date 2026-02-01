class Solution:
    def countSeniors(self, details: list[str]) -> int:
        seniors: int = 0

        for detail in details:
            baseNumber = int(detail[11])
            secondNumber = int(detail[12])
            age: int = baseNumber * 10 + secondNumber

            if age <= 60:
                continue

            seniors += 1

        return seniors


sol = Solution()
print(sol.countSeniors(["7868190130M7522", "5303914400F9211",
                        "9273338290F4010"]))
