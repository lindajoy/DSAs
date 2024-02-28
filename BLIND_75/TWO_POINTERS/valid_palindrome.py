"""
VALID PALINDROME

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
# What does isalnum() do?

# If all characters in the string are either letters (from a to z) or numbers (from 0 to 9), the method returns True.
# Example:

random_str = "7h9R2p5Q"
# Returns true or false is isalnum() returns true or false if the string contains numbers/strings.
lst = [i for i in random_str if i.isalnum()]
print(lst)

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