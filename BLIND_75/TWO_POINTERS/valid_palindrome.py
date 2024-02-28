"""
VALID PALINDROME

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isValidPalindrome(str):
   str = "".join(item for item in str if item.isalnum()).lower()
   left = 0
   right = len(str) - 1

   while left < right:
      if str[right] == str[left]:
         right -= 1
         left += 1
      else:
         return False
   return True

print(isValidPalindrome("A man, a plan, a canal: Panama"))