"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
Note: A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

# In this case we are given an array of numbers.
# The output should be the maximum sum

# A subarray is contingous...
# This is the Brute Force Solution
def maximumSubarray(nums):
   max_sum = float('-inf')
   n = len(nums)

   for i in range(n):
    for j in range(i, n):
        # Calculate the sum of the subarray
        subarray_sum = sum(nums[i:j+1])
        max_sum = max(max_sum, subarray_sum)

   return max_sum
   
print(maximumSubarray( [-2, 1, -3, 4, -1, 2, 1, -5, 4]))