"""
VALID PARENTHESES

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def isValid(str):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in str:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
            else:
                return False

        return not stack