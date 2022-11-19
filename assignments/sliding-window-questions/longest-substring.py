"""
Link to question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Difference between a subsequence and a substring:

1) A substring - a contiguous(continuous) sequence of characters present within a string. 
                   It is a string present inside a string.

2) A subsequence  - is a sequence that can be derived from another sequence of elements 
                    without changing the order of the remaining elements

For Example: {A, B, D} is one of the subsequences of the sequence {A, B, C, D, E} obtained after removing {C} and {E}.

For reference: https://www.codingninjas.com/codestudio/library/subsequence-vs-substring

"""

# Solution 1: Naive approach(Brute Force Algorithms)

# Solution 2: Sliding window technique

def lengthOfLongestSubstring(s: str):
    '''
    Why do you use set() data type?

    Sets are unordered and unstructured and do not allow duplicate values.
    '''

    charSet = set() 
    left = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[r])
        # max returns the maximum value in an iterable.
        res = max(res, r - left + 1) 
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(len('hello')) # outputs 5 the number of characters in the string.

print(max(5,10,9)) # outputs the maximum value in an iterable.

'''
Simple reminder of a for loop; how it works, how to loop through a string.
'''
s = 'hello'
for i in range(len(s)):
    print(s[i])