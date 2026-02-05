class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell

            sell += 1

        return max_profit


sol = Solution()
print(sol.maxProfit([5, 1, 5, 6, 7, 1, 10]))
