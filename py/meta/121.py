class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # msale = [prices[-1]]
        # for i in range(len(prices)-2,-1,-1):
        #     msale.append(prices[i] if prices[i] >= msale[-1] else msale[-1])
        # msale = msale[::-1]
        # mprofit = 0
        # for i in range(len(prices)):
        #     mprofit = max(mprofit,msale[i]-prices[i])
        # return mprofit
        buy, sell, mprofit = 0, 1, 0
        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            if currProfit <= 0:
                buy = sell
            else:
                mprofit = max(mprofit, currProfit)
            sell += 1
        return mprofit
