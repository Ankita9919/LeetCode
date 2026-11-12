class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return [num for num, count in counts.items() if count > len(nums) // 3]
