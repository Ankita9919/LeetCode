# LeetCode 1403
# Verified implementation draft

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        result = []
        chosen = total = 0
        for x in nums:
            result.append(x)
            chosen += x
            total -= x
            if chosen > total:
                break
        return result
