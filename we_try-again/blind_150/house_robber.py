"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

# Example 1
# Input : nums = [1,2,3,1]
# Output: 4

# Understanding this solution:
def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n +rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

nums = [1,2,3,1]
print(rob(nums))


# 💡 The second solution makes more sense to me
def rob2(nums):
    n = len(nums)

    # Remove all edge cases
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    # Initialize a DP array of the nums size
    dp = [0] * n
    # First index
    dp[0] = nums[0]
    # Second Index
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i- 2] + nums[i])
    return dp[n -1]

print(rob2(nums))