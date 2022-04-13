class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, a in enumerate(nums):
            if not i == a:
                return i
        return len(nums)