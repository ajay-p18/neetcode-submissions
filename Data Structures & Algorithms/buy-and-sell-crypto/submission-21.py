class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        j = 1
        maxProf = 0

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            
            else:
                profit = prices[j] - prices[i]
                maxProf = max(profit, maxProf)

            j += 1
        
        return maxProf
