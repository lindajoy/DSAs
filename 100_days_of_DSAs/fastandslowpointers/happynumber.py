"""
Write an algorithm to determine if a number n is a happy number.
We use the following process to check if a given number is a happy number:
Starting with the given number n, replace the number with the sum of the squares of its digits.
Repeat the process until:The number equals 1, which will depict that the given number n is a happy number.
It enters a cycle, which will depict that the given number n is not a happy number.
Return TRUE if n is a happy number, and FALSE if not.
"""
"""
Is 28 a happy number?
68 -> 100
4 -> 16 -> 37 -> 58 -> 
"""
# Pseudocode
# 1. Initialize a variable slow with the input number and fast with the squared sum of the input number's digit.
# 2. If fast is not 1, and not equal to slow increment slow by one iteration and fast by two iterations.
# 3. If fast converges to 1, return true otherwise return false

def is_happy_number(n):
    slow = n
    fast = sumOfSquared(n)

    while fast != slow:
        if fast == 1:
            return True
        else:
            slow = sumOfSquared(n)
            fast = sumOfSquared(fast)
    return False


def sumOfSquared(n:int) -> int:
    output = 0
    while n:
        digit = n % 10
        digit = digit **2
        output += digit
        n = n // 10
    return output

    
