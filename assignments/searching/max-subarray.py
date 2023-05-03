"""
Given an integer array, nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Note: A subarray is a contiguous part of an array.

💡 EXAMPLE I
array => [-2,1,-3,4,-1,2,1,-5,4]
subArray => [4,-1,2,1]

Pseudocode:
1. Find the sum of the whole array = that will be the (max)
2. 

"""
x = [-2, 1, -3, 4, -1 ,2 ,1 ,-5 ,4]
print('🤔',sum(x))

def maxSubArray(nums):
    maxSum = sum(nums)
    leftPtr = 0
    rightPtr = len(nums) - 1

    
