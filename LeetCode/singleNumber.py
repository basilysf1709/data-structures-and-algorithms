class Solution:
    def singleNumberEfficient(self, nums: List[int]) -> int:
        logicGate = 0
        for num in nums:
            logicGate ^= num
        return logicGate
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i