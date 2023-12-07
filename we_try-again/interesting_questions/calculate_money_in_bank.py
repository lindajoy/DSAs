"""
CALCULATE MONEY IN LEETCODE BANK

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

"""
Comments: I honestly struggled through this question, despite it being an easy question. 
          Needs repitition
"""
# 💡 First iteration, This just solves for when the days equate to a week or less
def totalMoney(n):
    total = 0
    for i in range(n):
        sum = i + 1
        total += sum
    return total

print(totalMoney(4))

# 💡 Seconde Iteration...

# This is the brute force way meaning that the time complexity here will be: O(n) as the length of the range increases.
# The more time to execute increases!

def totalMoney2(n):
    # 1+2+3+4+5+6+7 = 28
    # 2+3+4+5+6+7+8 = 28 + 7
    # 3+4+5+6+7+8+9 = 28 + 7 + 7

    # Initialize the day 
    day = 0
    # Initialize the deposit
    deposit = 1
    # This is the end result to be output by the calculate money in bank.
    res = 0

    # The loop should go on if the day we are on is less than n
    while day < n:
        res += deposit
        deposit += 1
        day += 1

        # This means we are beginning a new week!
        if day% 7 == 0:
            print(day // 7)
            deposit = 1  + day // 7
    return res

print(totalMoney2(21))