class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, a in enumerate(nums):
            if not i == a:
                return i
        return len(nums)

    def missingNumberFastest(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)
    
    def youtubeSolutionUsingBinary(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)