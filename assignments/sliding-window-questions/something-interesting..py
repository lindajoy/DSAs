
"""
💡 Interesting thing I learnt today
"""
str1 = 'hello'
str3 = 'boomerangs'
str2 = 'lordofrings'

print(max(str1, str2, str3, key=len))

"""
Lets talk about the Longest Palindromic substring problem, Yes?

Given a string pal_string, return the longest palindromic substring in pal_string.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

"""
We need to come up with a Pseudocode:
1. Initialize an empty string longestsub = " "
"""

def LongestSubstring(str):
    # Initialize an longest string
    long_str = ""

    for i in range(len(str)):
        # Initialize a left and right Pointer
        left = right = i

        while left >= 0 and right < len(str) and str[left] == str[right]:
            sliced_str = str[left : right + 1]
            long_str = max(sliced_str, long_str, key=len)
            left -= 1
            right += 1

        left = i
        right = i + 1

        while left >= 0 and right < len(str) and str[left] == str[right]:
            sliced_str = str[left : right + 1]
            long_str = max(sliced_str, long_str, key=len)
            left -= 1
            right += 1

    return long_str

print(LongestSubstring('babad'))


           