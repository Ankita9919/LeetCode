# LeetCode 1470
# Verified implementation draft

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.extend([nums[i], nums[i + n]])
        return result
