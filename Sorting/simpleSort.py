from typing import List

def simpleSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

print(simpleSort([10, 10, -3, 3, 1, 5]))