"""
VALID ANAGRAM

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

def is_valid_anagram(s, t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if t in s:
        return True
    return False

print(is_valid_anagram("anagram", "nagaram"))
print(is_valid_anagram("rat", "car"))