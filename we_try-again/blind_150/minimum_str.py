"""
Minimum Length of String After Deleting Similar Ends.

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

    1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    3. The prefix and the suffix should not intersect at any index.
    4. The characters from the prefix and suffix must be the same.
    5. Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
"""

# 💡 Example 1

# Input: s = "ca"
# Output = 2

# 💡 Example 2

# Input: s = "cabaabac"
# Output = 0

# 💡 Example 3

# Input s = "aabccabba"
# Output = 3

# This is an interesting question. 🤔

# Leetcode link: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05

def minimumLength(s):
    # Initialize the left and the right pointers.
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        char = s[left]

        while left < right and s[left] == char:
            left += 1

        while right > left and s[right] == char:
            right -= 1

    return right - left + 1

# print(minimumLength("aabccabba"))
print(minimumLength('bbbaab'))