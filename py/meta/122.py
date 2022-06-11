class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, profit, d = 0, 0, len(prices) - 1
        while i < d:
            while i < d and prices[i + 1] <= prices[i]:
                i += 1
            buy = i
            while i < d and prices[i + 1] > prices[i]:
                i += 1
            sell = i
            profit += prices[sell] - prices[buy]
        return profit
