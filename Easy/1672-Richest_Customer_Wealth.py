# LeetCode 1672
# Verified implementation draft

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))
