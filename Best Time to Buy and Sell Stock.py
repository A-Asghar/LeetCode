# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Beats 98%  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/849498278/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        l ,r = 0, 1
        while(r<len(prices)):
            profit = prices[r] - prices[l]
            if(profit > 0):
                if(profit > max_profit):
                    max_profit = profit
            else:
                l=r
            r+=1            
        return max_profit
            

