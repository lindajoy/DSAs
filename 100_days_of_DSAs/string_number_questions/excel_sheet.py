"""
Python ord() function takes a string argument of a single Unicode 
character and return its integer Unicode code point value.
"""
x = ord("A")
print(x)
"""
Python chr() function takes an integer and returns the string representing a character at that code point.
Since chr() function takes an integer argument and converts it to character, there is a valid range for the input.
The valid range for the argument is from 0 through 1,114,111
ValueError will be raised if the input integer is outside that range.
"""
y = chr(65)
# print(chr(-10))
print(y)
print(chr(25))

"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 

Here is the link to leetcode question: https://leetcode.com/problems/excel-sheet-column-title/
"""
class Solution:
    def convertToTitle(columnNumber:int) -> str:
        # Initializing the string that should store our value
        res = ""
        # Looping through the columnNumber while its greater than 0
        # Reason being A starts at 1, not at index 0
        # Hence we are starting from columns which are greater than 0
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord("A") + offset)
            columnNumber = (columnNumber - 1) // 26
        # here we are reversing the string
        return res[::-1]
