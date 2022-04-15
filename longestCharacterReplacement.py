class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        setStr = {}
        res = 0
        l = 0
        for r in range(len(s)):
            setStr[s[r]] = 1 + setStr.get(s[r], 0)
            if (r - l + 1) - max(setStr.values()) > k:
                setStr[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res