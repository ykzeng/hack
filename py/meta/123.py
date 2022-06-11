class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, profit, d = 0, [], len(prices) - 1
        # while i < d:
        #     while i < d and prices[i + 1] <= prices[i]:
        #         i += 1
        #     buy = i
        #     while i < d and prices[i + 1] > prices[i]:
        #         i += 1
        #     sell = i
        #     if len(profit) >= 2:
        #         heapq.heappushpop(profit,prices[sell]-prices[buy])
        #     else:
        #         heapq.heappush(profit,prices[sell]-prices[buy])
        # return sum(profit)
        oneBuyOneSell = twoBuyTwoSell = 0
        oneBuy = twoBuy = float("inf")

        for p in prices:
            oneBuy = min(oneBuy, p)
            oneBuyOneSell = max(oneBuyOneSell, p - oneBuy)
            twoBuy = min(twoBuy, p - oneBuyOneSell)
            twoBuyTwoSell = max(twoBuyTwoSell, p - twoBuy)

        return twoBuyTwoSell
