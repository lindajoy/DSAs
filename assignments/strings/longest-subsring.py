'''
Given a string s, find the length of the longest substring without repeating characters.

Example one: "abcabcb"
        output: 3

Example two: ""pwwkew"
        output:3

Example three: ""pekkkekwww"
        output: 3


https://leetcode.com/problems/longest-substring-without-repeating-characters/
input: string
'''

"""
💡 First Solution

Brute Force approach: Two nested for loops
"""

def longestSubstring(string):
    maxlength = 0
