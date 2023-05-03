"""
You are a professional robber, and after weeks of planning, you plan to rob some houses along a street. 
Each of these houses has a lot of money and valuables.
Let’s say that you cannot rob houses adjacent to each other since they have security and burglar alarms installed.

Following the above mentioned constraint and given an integer array, nums, 
representing the amount of money in each house, 
return the maximum amount of money you can steal tonight without alerting the police.

Example:

nums = [1,2,3,1]

Output 4

"""

def maxAmountARobberCanRob(arr):
    rob1, rob2 = 0, 0

    for n in arr:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return 2


# print(maxAmountARobberCanRob([1,2,3,1]))

x = [1,2,3,5]

for i in x:
    print('🤔', i)


for i in range(len(x)):
    print(i)