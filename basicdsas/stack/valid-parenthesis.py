from . import stack
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

'''
Understanding Educative Proposed Solution.
'''

S = stack.Stack()

# Is Match Function
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_parent_balanced(parent_string):
    s = stack.Stack()
    is_balanced = True
    index = 0

    while index < len(parent_string) and is_balanced:
        paren = parent_string(index)
        if paren in '([{':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
                    break

        index += 1

    if s.is_empty and is_balanced:
        return True

    else:
        return False
