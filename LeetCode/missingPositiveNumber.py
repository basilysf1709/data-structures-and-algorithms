class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        count = 0
        while i < arr[len(arr) - 1]:
            if i + 1 not in arr:
                count += 1
                if count == k:
                    return i + 1
            if i + 1 == arr[len(arr) - 1]:
                return arr[len(arr) - 1] + k - count
            i += 1