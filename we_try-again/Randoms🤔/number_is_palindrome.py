"""
Builds up on question on this folder: reverse_digits.py

A palindromic string is one which reads the same forwards and backwards, e.g., "redivider". 
In this problem, you are to write a program which determines if the decimal representation of an integer is a palindromic string. 
For example, your program should return true for the inputs 0,1",7,17,727,333, a:nd21.4744741.2, arrd false for the inputs -'1,12,100, and 2147483647.

A number is not an iterable...
"""

# 💡 Had a dumb error, Please keep track of your variables!!

def isPalindrome(num):
    # Validate the input first
    if num < 0:
        return False
    
    reversed = 0
    original = num

    while num:
        digit = num % 10
        reversed = reversed * 10 + digit
        num =  num // 10
    return reversed == original

print(isPalindrome(11))
print(isPalindrome(1331))

