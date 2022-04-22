class Solution:
    def reverse(self, x: int) -> int:
        return (int(str(x)[::-1]) if x >= 0 else -1 * int(str(x)[::-1].replace('-', ''))) if (int(str(x)[::-1]) if x >= 0 else -1 * int(str(x)[::-1].replace('-', ''))) > pow(-2, 31) and (int(str(x)[::-1]) if x >= 0 else -1 * int(str(x)[::-1].replace('-', ''))) < pow(2, 31) + 1 else 0