"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.
"""

"""
💡 Example 1

Input: s = "()"
Output: true
"""

"""
💡 Example 2

Input: s = "()[]{}"
Output: true
"""

"""
💡 Example 3

Input: s = "(]"
Output: false
"""

"""
💡 First iteration of solution  => Did the basic minimum:

Considered that for a string to be a valid parentheses the length should always
be divisible by 2, If not it does not qualify to be a valid parenthesis.

And also if the string length is 2, I just compare the first and the second element in
the string.
"""
class StackPrac():
    def isValid(self, s):
        if len(s) == 2:
            return s[0] == s[1]
        elif len(s)%2 == 0:
            return False
            

myParanthesisVerifier = StackPrac()
mystring = '()'
mystring2 = '{ { )'

print(myParanthesisVerifier.isValid(mystring))
# print(myParanthesisVerifier.isValid(mystring2))