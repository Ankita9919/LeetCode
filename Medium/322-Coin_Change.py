class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] = min(dp[value], dp[value - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
