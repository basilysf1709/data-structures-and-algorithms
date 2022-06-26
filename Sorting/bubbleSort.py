from typing import List

# put the max element at the end 

def swap(nums: List[int], a: int, b: int) -> None:
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

def bubbleSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums

print(bubbleSort([10,9,8,7,6,5,4,3,2,1]))