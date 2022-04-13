class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        listSum = []
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                k = 0
                if i == j:
                    j += 1
                    continue
                while k < len(nums):
                    if i == k or j == k:
                        k += 1
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        tmp.sort()
                        if tmp not in listSum:
                            listSum.append(tmp)
                    k += 1
                j += 1
            i += 1
        return listSum