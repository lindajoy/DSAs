"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

def longestPalindromicString(s):
    # If string is of length 1 or less than zero, then we just return the string.
    if len(s) <= 1:
        return s
    
    # Initialize the maximum length to 1
    max_length = 1
    max_str = s[0]

    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if j-i + 1 > max_length and s[i:j+1] == s[i:j+1][::-1]:
                max_length = j - i + 1
                max_str = s[i: j +1]
    return max_str
Input = "babad"
#Output: "bab"
print(longestPalindromicString(Input))