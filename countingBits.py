class Solution:
    def countBits(self, n: int) -> List[int]:
        countBits = []
        listOfNum = range(0, n + 1)
        for i in listOfNum:
            countBits.append(bin(i).count('1'))
        return countBits