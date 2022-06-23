class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]