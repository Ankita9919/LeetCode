# LeetCode 1480
# Verified implementation draft

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []
        for x in nums:
            total += x
            result.append(total)
        return result
