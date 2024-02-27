"""
PALINDROME CHECK

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. 
Note that single-character strings are palindromes.

"""
string1 = "abcdcba"

# Simplest way to check whether a string is a palindrome
print(string1 == string1[::-1])

# But we can not do it this way in an interview unless the interviewer allows it.
def checkIsPalindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

print(checkIsPalindrome("abcdcba"))
print(checkIsPalindrome("radar"))
print(checkIsPalindrome("hello"))