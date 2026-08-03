class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        l = 0
        r = 1

        while (r < len(prices)):
            curr = prices[r] - prices[l]
            if curr > 0:
                profit = max(profit, curr)
            else:
                l = r
            r += 1
        
        return profit

