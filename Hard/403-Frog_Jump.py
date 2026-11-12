class Solution:
    def canCross(self, stones: list[int]) -> bool:
        positions = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for step in (jump - 1, jump, jump + 1):
                    if step > 0 and stone + step in positions:
                        dp[stone + step].add(step)

        return bool(dp[stones[-1]])
