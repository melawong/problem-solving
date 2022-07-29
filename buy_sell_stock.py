class Solution:
    def maxProfit(self, prices):
        buyPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < buyPrice:
                buyPrice = price
            if price - buyPrice > maxProfit:
                maxProfit = price-buyPrice
        return maxProfit
