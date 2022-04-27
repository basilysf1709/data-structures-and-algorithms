class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for a in t:
            if s.count(a) != t.count(a):
                return a