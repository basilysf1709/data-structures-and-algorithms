class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                nums.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                nums.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                nums.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                nums.append(matrix[i][left])
            left += 1
        return nums
            