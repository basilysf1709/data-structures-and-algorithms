class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2, sum3, sum4 = 0, 0, 0, 0
        if len(nums) == 1: return nums[0]
        for i in range(len(nums) - 1):
            temp = max(nums[i] + sum1, sum2)
            sum1 = sum2
            sum2 = temp
        for i in range(1, len(nums)):
            temp = max(nums[i] + sum3, sum4)
            sum3 = sum4
            sum4 = temp
        return max(sum2, sum4)