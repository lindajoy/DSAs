"""
My solution on leetcode did not work, due a time exceeded error, lets find out why.

Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""
"""
My first solution was this:
 Step I: Initialize a left and right pointer, also had a count variable(see below) and traverse through the string
"""

class SolutionOne(object):
    def validPalindrome(s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                count += 1
            else:
                count = 0

        return count

class Solution(object):
    def validPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

x = Solution()
b = 'aba'
print(Solution.validPalindrome(b))
