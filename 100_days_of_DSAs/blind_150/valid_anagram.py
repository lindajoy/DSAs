"""
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
"""
PROBLEM DESTRUCTURING
Input: Two strings
Output: is  a boolean
We can choose to sort the the strings
"""

def validAnagram(s, t):
    # Here there are two strings that may be similar in structure
    s_sorted =  ''.join(sorted(s))
    t_sorted = ''.join(sorted(t))

    if s_sorted == t_sorted:
        return True
    
    return False
