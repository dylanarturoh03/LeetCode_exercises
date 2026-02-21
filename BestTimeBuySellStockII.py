class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit: int = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    
    def maxProfit_mver(self, prices: list[int]) -> int:
        profit = 0
        n = len(prices)
        i = 0

        while i < n - 1:

            # Find local minimum (buy)
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1

            buy = prices[i]

            # Find local maximum (sell)
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1

            sell = prices[i]

            profit += sell - buy

        return profit


sol = Solution()
print(sol.maxProfit_mver([7,1,3,2,4,6]))
