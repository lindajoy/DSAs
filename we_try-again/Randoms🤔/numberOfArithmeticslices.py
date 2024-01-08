"""
An integer array is called arithmetic if it consists of at least three elements 
and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
"""

# EXAMPLE 1
#
# Input : nums = [1,2,3,4]
# Output: 3
# We have 3 arithmetic slices in nums: [1,2,3], [2,3,4], [1,2,3,4]

# EXAMPLE 2
#
# Input : nums = [1]
# Output: 0

# 💡 First step would be to remove or not to execute arrays that have a length shorter than 2

def numberOfArithmeticSlices(nums):
    # Check off arrays with length of 1 or 2
    if len(nums) == 1 or len(nums) == 2:
        return 0
    # Initialize the lenght of nums
    n = len(nums)
    # Initialize an empty dp array
    dp = [0] * n

    for i in range(2,n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i-1] + 1
    return sum(dp)

    
# print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2, 3,4]))

# Lets understand something here..
nums2 = [1,2,3,4,5,6]

# for i in range(2, len(nums2)):
#     print(i)

# When it comes to the range function we usually use the SES acronynm which means: Start, End, Step
# We can do some thing like
    
# for i in range(20,30,3):
#     print(i)