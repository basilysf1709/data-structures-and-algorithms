class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = nums.count(val)
        length = len(nums)
        while i < k:
            nums.remove(val)
            i += 1
        return length - k