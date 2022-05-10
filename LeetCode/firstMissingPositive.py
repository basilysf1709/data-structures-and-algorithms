class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in (range(len(nums))):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums) + 1 and nums[i] != 0:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
                elif nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -1 * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1