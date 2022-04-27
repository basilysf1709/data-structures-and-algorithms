from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        least = [amount + 1] * (amount + 1)
        least[0] = 0
        for i in range(1, amount + 1):
            print(str(i) + ':')
            for c in coins:
                if i - c >= 0:
                    least[i] = min(least[i], 1 + least[i - c])
        return least[amount] if least[amount] != amount + 1 else - 1

s = Solution()
print(s.coinChange([1,2,5], 11))
