"""
Squares of Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""
# This is the Easiest solution.
# But this solution seems to be easy for a real solution in an interview.

def squares_of_sorted_array(nums):
    squared = [ i * i for i in nums ]
    return sorted(squared)

print(squares_of_sorted_array([-4,-1,0,3,10]))


# SECOND SOLUTION
# Using Two Pointers/ Rather like the MIT professor says the Two Fingers approach ✌🏽.
# This is actually a better way of doing it. 🤔

def squares_of_sorted_array_2(nums):
    n = len(nums)
    ans = [0] * n
    start, end = 0, len(nums) - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[start]) >=  abs(nums[end]):
            ans[i] = nums[start] * nums[start]
            start += 1
        else:
            ans[i] = nums[end] * nums[end]
            end -= 1
    return ans

print(squares_of_sorted_array_2([-4,-1,0,3,10]))




