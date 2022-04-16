class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        listPascal = []
        while i < numRows:
            j = 0
            indivList = []
            while j <= i:
                if i == 0 or i == 1 or j == 0 or j == i:
                    indivList.append(1)
                else:
                    indivList.append(listPascal[i - 1][j - 1] + listPascal[i - 1][j])
                j += 1
            listPascal.append(indivList)
            i += 1
        return listPascal