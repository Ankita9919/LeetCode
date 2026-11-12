# LeetCode 1431
# Verified implementation draft

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        largest = max(candies)
        return [x + extraCandies >= largest for x in candies]
