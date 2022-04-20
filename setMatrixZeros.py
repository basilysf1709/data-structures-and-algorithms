class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indicesX = []
        indicesY = []
        for i, a in enumerate(matrix):
            for j, b in enumerate(a):
                if b == 0:
                    indicesX.append(i)
                    indicesY.append(j)
        
        for i, a in enumerate(matrix):
            for j, b in enumerate(a):
                if i in indicesX or j in indicesY:
                    matrix[i][j] = 0