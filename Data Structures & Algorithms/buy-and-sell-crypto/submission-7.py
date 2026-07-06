class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        MaxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
             profit = prices[right] -prices[left]
             MaxProfit = max(profit, MaxProfit)
            else:
                left = right
            right +=1

        return MaxProfit



       