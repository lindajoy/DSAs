'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''

"""
💡 My Solution

What are the inputs = string 

Input: s = "()"
Output: true


Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Steps To Take:

I first look at the length of the string entered if the string length 
is equal or divisible to two, then this can go to the next step which is 
validating whether the string entered is a valid parentheses or not.

"""

def isValidParantheses(s):
    string_length = len(s)
    
    if string_length%2 == 0:
        return True
    else:
        return False


print(isValidParantheses('()'))
print(isValidParantheses( "()[]{}"))
print(isValidParantheses("(]"))

class isValidParenthesis():
    def __init__(self, s):
        self.s = s
        print(s)
    
    def isString(self) -> str:
        return f"{self.s}"


isValid  = isValidParantheses('hello')
