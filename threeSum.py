class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
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
    
    def threeSumMyFirstAttempt(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        listSum = []
        i = 0
        while i < len(nums):
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                tmp = [nums[i], nums[lp], nums[rp]]
                if sum(tmp) < 0:
                    lp += 1
                elif sum(tmp) > 0:
                    rp -= 1
                else:
                    if tmp not in listSum:
                        listSum.append(tmp)
                    lp += 1
                    rp -= 1
            i += 1
        return listSum