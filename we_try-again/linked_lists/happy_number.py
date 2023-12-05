"""
Write an algorithm to determine if a number n is a happy number.
We use the following process to check if a given number is a happy number:
Starting with the given number n, replace the number with the sum of the squares of its digits.

Repeat the process until:
    =>The number equals 1, which will depict that the given number n is a happy number.
    =>It enters a cycle, which will depict that the given number n is not a happy number.

Return TRUE if n is a happy number, and FALSE if not.
"""


def isHappyNumber(n):
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

    # 💡 Recursive way
    # while n:
    #     digit = n % 10
    #     digit = digit **2
    #     output += digit
    #     n = n // 10
    # return output

    # USING DIVMOD
    ans = divmod(n, 10) # Returns a tuple!(Quotient, remainder) (Hehe)
    for i in ans:
        output += i ** 2
    return output

    
print(isHappyNumber(23))

s = b = 23

while s == b:
    s = 45

# print(s)
# print(b)
# print(id(s))
# print(id(b))

def sumOfSquared2(n:int) -> int:
    output = 0
    s = divmod(n, 10)
    for i in s:
        output += i ** 2
  
    return output

print(sumOfSquared2(12))
