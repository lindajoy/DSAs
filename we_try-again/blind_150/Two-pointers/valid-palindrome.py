"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
"""
Input: A string
Output: Boolean

Sample String = s = "A man, a plan, a canal: Panama"

isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter(a-z) and numbers(0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc.
"""

Sample_String = s = "A man, a plan, a canal: Panama"
# print(Sample_String, s)


# for i in Sample_String:
#     print('I am a character in my string', i)

print("A" == "a")

def isPalindrome(s):
    string_lower = s.lower()
    right = 0
    left = len(s) - 1
    
    while right <= left:
        if string_lower[right].isalnum() == False:
            right += 1
        elif string_lower[left].isalnum() == False:
            left -= 1
        elif string_lower[left] == string_lower[right]:
            left -= 1
            right += 1
    return True


print('Hello, Is Palindrome function has been called:',isPalindrome(s))