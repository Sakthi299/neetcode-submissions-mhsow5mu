class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = prices[0] # this should be minimum price to buy
        profit = 0 # it should maximum

        
        for i in range(1, len(prices), 1):
            minBuy = prices[i] if prices[i] < minBuy else minBuy
            if prices[i] > minBuy:
                profit = max(profit, prices[i]-minBuy)
            
        return profit
