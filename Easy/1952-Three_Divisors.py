# LeetCode 1952
# Verified implementation draft

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        root = int(n ** 0.5)
        return root * root == n and all(root % d for d in range(2, int(root ** 0.5) + 1))
