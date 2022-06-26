from typing import List

# swap the starting elements by the smallest element left

def swap(nums: List[int], a: int, b: int) -> None:
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

# finding the index of the smallest number
def findSmallest(nums: List[int], a: int) -> int:
    minimum = a
    for i in range(a, len(nums)):
        if nums[i] < nums[minimum]:
            minimum = i
    return minimum

def selectionSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        index = findSmallest(nums, i)
        swap(nums, index, i)
    return nums
    
print(selectionSort([100, 9, -12, -23, -12, -10, -1, 2, -1, 123]))
