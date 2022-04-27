class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        length = len(matrix)
        temp = [[0] * length for i in range(length)]
        while i < length:
            counter = 0
            j = length - 1
            while j >= 0:
                temp[i][counter] = matrix[j][i]
                j -= 1
                counter += 1
            i += 1
        matrix.clear()
        for a in temp:
            matrix.append(a)