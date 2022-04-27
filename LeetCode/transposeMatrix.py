import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp = []
        i = 0
        while i < len(matrix[0]):
            j = 0
            while j < len(matrix):
                temp.append(matrix[j][i])
                j += 1
            i += 1
        return np.reshape(temp, (len(matrix[0]),len(matrix)))