import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for x in string.punctuation:
            s = s.replace(x, '')
        s = s.replace(' ', '')
        s = s.lower()
        if s == s[::-1]:
            return True
        return False
    def isPalindromeUsingTranslate(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(' ', '')
        s = s.lower()
        if s == s[::-1]:
            return True
        return False