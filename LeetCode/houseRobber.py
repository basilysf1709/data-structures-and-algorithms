class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for n in nums:
            temp = max(sum1 + n, sum2)
            sum1 = sum2
            sum2 = temp
        return sum2