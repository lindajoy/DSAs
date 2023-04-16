"""
Given an integer array, nums, return the length of the longest strictly increasing subsequence.

Link: https://www.educative.io/courses/grokking-coding-interview-patterns-python/q2zMRZB4D23

First encounter with Dynamic Programming:

What is Dynamic Programming? 

Dynamic programming technique where an algorithimic problem is first broken down
into sub problems, the results are saved and then the sub-problems are optimized to find 
the overall solution - which usually has to do with finding the maximum and minimum range of the 
algorithimic query.

"""

"""
INPUT HERE IS: AN ARRAY : nums = [10,9,2,5,3,7,101,18]

OUTPUT HERE IS THE LONGEST INCREASING SUBSEQUENCE : 4

ARRAY HERE WOULD BE: [2,3,7,101]
"""

def longest_subsequence(nums):
    # Creating this array for storing the cached lengths at each index.
    # Here we initialize an empty array of the assumed length at each index.

    longest_sub = [1] * len(nums) 
    print('Original List',longest_sub)

    # Loop the entire array from reverse order
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if (nums[i] < nums[j]):
                longest_sub[i] = max(longest_sub[i], 1 + longest_sub[j])

    return max(longest_sub)

nums_array = [10,9,2,5,3,7,101,18]
print(longest_subsequence(nums_array))

"""
💡 SOLUTION ANALYSIS

Time Complexity here is Quadratic since we have two loops, 
One outer loop and one inner loop to compare the curr and prev integers.
"""