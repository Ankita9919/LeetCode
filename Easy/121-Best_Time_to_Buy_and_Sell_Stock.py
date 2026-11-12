# LeetCode 121
# Verified implementation draft

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float("inf")
        profit = 0
        for price in prices:
            low = min(low, price)
            profit = max(profit, price - low)
        return profit
