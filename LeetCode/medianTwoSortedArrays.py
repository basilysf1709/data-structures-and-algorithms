class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        return (float(nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])) / 2 if len(nums1) % 2 == 0 else float(nums1[len(nums1)//2])