class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r = 0,1
        max_price = 0

        while r < len(prices):
            sell_price = prices[r] - prices[l]
            if sell_price < 0:
                l=r
            
            max_price = max(sell_price, max_price)
            r+=1

        return max_price
