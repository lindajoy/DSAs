"""
Leetcode Question Link: https://leetcode.com/problems/valid-parenthesis-string/description/

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""

# Whats the input? A string.

# Whats the Output? A Boolean indicating whether the string is a valid parentheses or not.

# Example 1

# Input: s = '()'
# Output: True

# Example 2:

# Input: s = '(*)'
# Output: True

# Example 3

# Input: s = "(*))"
# Output: True

# s = 1 or 2 or 3

# no_1 = 3
# print(s == no_1)


# Lets go back to valid parantheses question 1 => What are we trying to achieve on this question.

# Understand more on Stacks.

# Question goes like this:
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

def is_well_formed(s):
    # Initialze an empty list and a dictionary that points a 'key' opening bracket to value:its closing bracket
    left_chars, lookup = [], {'(' : ')', '{' :'}', '[': ']'}
    for c in s:
        # Just looks up the keys.
        if c in lookup:
            left_chars.append(c)
        # Check whether the key: points to value c.
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False
    return len(left_chars) == 0

print(is_well_formed('()[]{}'))

# Lets break this down:
# Given our input is: ()
# Just the first iteration to ensure that we capture the logic well:
# leftchar = ["("]
# leftchar.pop() => Outputs the value: "()"
# lookup["("]


# Say when you do something like this:
lst = [2, 3]


print(lst.pop())
print(lst)

# Another thing which i find interesting is
places_of_work = { "Joy": "Google", "Ann": "Mastercard", "Justin": "Microsoft"}

# This one checks if a particular key exists in a dictionary
if "Joy" in places_of_work:
    print("Joy to the world!")

# This one wont print out anything since Google is a value not a key.
if "Google" in places_of_work:
    print('Joy is Joining google in July')
