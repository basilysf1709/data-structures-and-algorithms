from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs[0])):
            for s in strs:
                # print(s)
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            print(result)
            result += strs[0][i]
        return result

s = Solution()
print(s.longestCommonPrefix(["flow","flower","glow"]))