"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Whats the input? A string.
# Whats the output? The length of the longest substring without non repeating characters.


def lengthOfLongestSubstring(s):
    left = 0
    hashset = set()
    max_length = 0
    n = len(s)

    for right in range(n):
        if s[right] not in hashset:
            hashset.add(s[right])
            max_length = max(max_length, right -left +1)
        else:
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
    return max_length

print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring("abcabcbb"))