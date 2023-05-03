"""
We are given two strings, s and t. The minimum window substring of t in s is defined as follows:It is the shortest substring of s that includes all of the characters present in t.

The frequency of each character in this substring that belongs to t should be equal to or greater than its frequency in t.

The order of the characters does not matter here.We have to find the minimum window substring of t in s.

Example 1:          
s = "AbabbbAbaA"
t = "Bab"

returns ''
"""

def findMinimumSubstring(s, t):

    if len(t) == 0:
        return ""

    leftPtr = 0
    rightPtr = 0

    # Create a hashset that keeps count of t
    hashT = {}

    for character in t:
        if character in hashT:
            hashT[character] += 1
        else:
            hashT = 1

    return hashT

print(findMinimumSubstring('Hello', "Mellow"))



