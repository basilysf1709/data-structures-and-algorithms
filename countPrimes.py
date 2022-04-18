class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        i = 2
        count = 0
        while i < n:
            j = i - 1
            flag = 0
            if i % 2 == 0 and i != 2:
                flag = 1
            else:
                while j > 0:
                    if i % j == 0 and j > 1:
                        flag = 1
                        break
                    j -= 1
            if flag == 0:
                count += 1
            i += 1
        return count
s = Solution()
print(s.countPrimes(499979))