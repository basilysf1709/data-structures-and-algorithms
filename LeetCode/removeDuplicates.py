class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                j = nums.count(i)
                while j > 1:
                    nums.remove(i)
                    j -= 1
        print(nums)
        return len(nums)