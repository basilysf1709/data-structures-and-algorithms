class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        prev = []
        res = [int(n) for n in str(n)]
        prev.append(res)
        while 1:
            sum = 0
            for i in res:
                sum += int(i) * int(i)
            res = [int(sum) for sum in str(sum)]
            if res in prev:
                return False
            prev.append(res)
            if sum == 1:
                return True