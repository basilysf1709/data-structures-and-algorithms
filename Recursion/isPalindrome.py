def isPalindrome(s: str) -> str:
    if len(s) == 0 or len(s) == 1: return True
    elif s[0] == s[len(s) - 1]: return isPalindrome(s[1:len(s) - 1])
    return False

print(isPalindrome("racecar"))