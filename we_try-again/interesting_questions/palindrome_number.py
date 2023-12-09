"""
Given an integer x, return true if x is a palindrome, and false otherwise.

EXAMPLE 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

EXAMPLE 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""

"""
😄🤣 Something to note here is that a number is not an iterable. 
        => Almost fell into the pits, trying to execute this question by assuming a number is an iterable.
        (That was my first thought btw 🤔)

So, the other way could be Reversing the Entire Number, then check whether its equal to the original input.

Questions for the Interviewer at this point:
    1. Can the input or the number we expect a negative number?
       Right now, we can assume that if the number is negative, it cannot be a palindrome.

    2. Initialize two variables:
        * reversed: The variable will store the reversed value of the number x
        * temp: The variable is a temporary placeholder to manipulate the number without modifying the original value.

    3. We can enter a loop that cntinues untill temp becomes zero:
        * Inside the loop, we extract the last digit of temp using the modulo operator and store it in the digit variable.
        * To reverse the number, we multuply the current value of reversed by 10 and add the extracted digit
        * We then divide, tempy by 10 to remove the last digit and move on to the next iteration.

    4. Once the loop is completed, we have reversed the entire number. Now we compare the reversed value reversed with the original
       input value x.
"""

"""
I really like the idea of recursive/iterative functions !!!
"""

def is_int_palindrome(x):
    # Remove the edge case here
    if x < 0:
        return False
    
    reversed_num = 0
    temp = x

    # Recursive function that calls itself whenever the value temp is not equal to 0.
    while temp != 0:
        # Returns the remainder when a number is divided by 10
        digit = temp % 10
        reversed_num = reversed_num* 10 + digit
        # Returns the whole digit when divided by 10.
        temp //= 10

    return reversed_num == x

print(is_int_palindrome(121))