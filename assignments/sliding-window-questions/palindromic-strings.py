"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Pseudocode:
1.
2.
3.
"""

def countSubstrings(str):
    # Initialize the substring count
    res = 0

    for i in range(len(str)):
        # This block calculates the odd palindromes in a substring
        left = right = i

        while left >= 0 and right < len(str) and str[left] == str[right]:
            res += 1
            left -= 1
            right += 1

        # This block calculates the even palindromes in a substring
        left = i
        right = i + 1

        while left >= 0 and right < len(str) and str[left] == str[right]:
            res += 1
            left -= 1
            right += 1

    return res


x = "aaa"
print(countSubstrings(x))


class Solution:
    def calculateNumberOfSubstrings(self, str2):
        res = 0
        for i  in range(len(str2)):

            res += self.calculatePalindrome(str2,i, i )
            res += self.calculatePalindrome(str, i, i+1)

        return res
 

    def calculatePalindrome(self, s, l, r):
        res = 0

        while l >= 0 and r < len(s) and str[l] == str[r]:
            res += 1
            l -= 1
            r += 1

        return res



        
        
