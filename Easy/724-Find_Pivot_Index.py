# LeetCode 724
# Verified implementation draft

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            right -= x
            if left == right:
                return i
            left += x
        return -1
