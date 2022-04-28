from typing import List
def binarySearch(nums: List[int], left: int, right: int, target: int) -> bool:
    if left > right: return False
    mid = (left + right) // 2
    if target == nums[mid]: return True
    if target < nums[mid]: return binarySearch(nums, left, mid - 1, target)
    return binarySearch(nums, mid + 1, right, target)


nums = [1,2,4,5,6,7,8]

print(binarySearch(nums,0,len(nums) - 1,90))