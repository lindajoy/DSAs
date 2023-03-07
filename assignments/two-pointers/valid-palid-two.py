"""
Write a function that takes a string as input and 
checks whether it can be a valid palindrome by removing at most one character from it.
"""

'''
Pseudocode =>
1. Iinitialize the right
'''

def is_palindrome(s):
  left, right = 0, len(s) -1

  while left < right:
    if s[left] != s[right]:
        skipLeft, skipRight = s[left + 1: right + 1], s[left:right]
        return (skipLeft == skipLeft[::-1]) or skipRight == skipRight[::1]
   
    left, right = left+1, right -1

  return False

print('One',is_palindrome('madame'))

''' 
My Simple list
'''
x = ['a','b']
x.append('c')
print(x)
x.insert(0, 'd')
print(x)