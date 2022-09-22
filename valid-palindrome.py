"""
Valid Palindrome: https://leetcode.com/problems/valid-palindrome/
"""

"""
First attempt: Works with strings with no punctuation marks😊
"""
def is_palindrome(str):
    a = str
    print(a)
    b = ''.join(reversed(str))
    print(b)
    if a == b:
       return True
    else:
        return False

print(is_palindrome('mom'))
print(''.join(reversed('mom')))
h