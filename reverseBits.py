class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = "{:032b}".format(n)
        sum = 0
        for i, a in enumerate(tmp):
            sum += 2**i * int(a)
        return sum