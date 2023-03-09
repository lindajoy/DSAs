"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

"""
💡 First attempt accepted by leetcode
"""
class Solution(object):
    def isHappy(self, n):    
        slow = n
        fast = self.sumOfSquares(n)

        while  fast != slow:
            if fast == 1:
                return True
            else:
                slow = self.sumOfSquares(n)
                fast = self.sumOfSquares(fast)

        return False
       

    def sumOfSquares(self, n:int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


x = Solution()

print(x.isHappy(19))
print(x.isHappy(2))
print(x.isHappy(4))