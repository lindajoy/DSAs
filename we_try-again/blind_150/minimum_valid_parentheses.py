"""
💡 MINIMUM VALID PARENTHESES.

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""

# The task is to remove the minimum number of parentheses, in any position so that the resulting string is valid.

# What is the Input? A string
# What is the Ouput? A string

def removeMinimumParentheses(str):
    if not str or len(str) == 0:
        return ''
    
    # We expect an invalid string, with invalid number of parentheses.
    # lee(t(c)o)de)