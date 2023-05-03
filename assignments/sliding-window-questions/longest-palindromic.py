"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

def LongestPalindrome(s):
    start, end = 0, len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            s = s[start + 1: end]
            
        start, end = start + 1, end - 1

    return s

x = "babad"
y = "abcdefghgfe"
print('🤔',LongestPalindrome(y))
print(len(x))