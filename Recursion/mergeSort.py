from typing import List

def mergeSort(nums: List[int]) -> None:
    leftArr = nums[:len(nums) // 2]
    rightArr = nums[len(nums) // 2:]
    if len(nums) > 1:
        mergeSort(leftArr)
        mergeSort(rightArr)
        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                nums[k] = leftArr[i]
                i += 1
            else:
                nums[k] = rightArr[j]
                j += 1
            k += 1
        while i < len(leftArr):
            nums[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            nums[k] = rightArr[j]
            j += 1
            k += 1

nums = [2,3,5,1,7,4,4,4,2,6,0]
mergeSort(nums)
print(nums)

# Time Complexity: O(n * log(n))
# Space Complexity: O(n) or O(1) ???