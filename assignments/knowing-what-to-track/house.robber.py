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
    return rob2

# print(maxAmountARobberCanRob([2,7,9,3,1]))

def maxAmountRobberRobs2(arr):
    maxMoney = 0

    for i in range(len(arr)):
        sliced_arr = arr[i+2 : len(arr)]
        if (len(sliced_arr) > 0):
            max_on_sliced = max(sliced_arr)
        else: 
            max_on_sliced = 0

        temp = (arr[i] + max_on_sliced)

        maxMoney = max(temp, maxMoney)

    return maxMoney

# print(maxAmountRobberRobs2([1,2,3,1]))


def maxAmountRobberRobss(arr):
    # Assume that the rest of the houses are not there
    if not arr:
        return 0
    
    # Get length of the array
    n = len(arr)

    # Initialize an empty list to store the maximum values
    dp = [0] * (n+1)

    # Base case where the first value in the array is zero
    dp[0] = 0

    # First value in the array
    dp[1] = arr[0]

    # Iterate through the rest of the arrays
    for i in range(2, n + 1):
        print("DP => Instance 1:", dp[i-1])

        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])


    return dp[n]

print(maxAmountRobberRobss([2,7,9,3,1]))


x = [1,2,3,5]

# for i in x:
#     print('🤔', i)


# for i in range(len(x)):
#     print(i)