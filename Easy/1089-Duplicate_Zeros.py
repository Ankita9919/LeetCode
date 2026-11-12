# LeetCode 1089
# Verified implementation draft

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        result = []
        for x in arr:
            result.append(x)
            if x == 0:
                result.append(0)
        arr[:] = result[:len(arr)]
