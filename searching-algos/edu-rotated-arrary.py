"""
You’re given a rotated sorted array arr in ascending order so that after the first rotation, 
the last element of the array will be shifted to the starting position and so on. 
For the given array (containing unique elements), your task is to find the minimum element of this array.


Note: The algorithm must be written so that it runs in O(logn) time.

"""
"""
💡 Example 1
[23, 41, 47, 51, 19, 21]

Returns 19
The array has been rotated four times.

💡 Example 2
[5, 7, 11, 2, 3]

Returns 2
The array has been rotated three times.

"""

"""
Notes from soln:

First whenever your are asked for solution that runs on O(logn) time => This has to be a divide and conquer solution.
"""

def find_nums(nums):
    start, end = 0 , len(nums) - 1

    midIndex = (start + end) // 2

    # This means the array has not been sorted.
    if nums[start] < nums[end]:
        return 0

    while start < end:
        if nums[midIndex] < nums[midIndex - 1]:
            return nums[midIndex]

        if nums[midIndex] >= nums[start]:
            low += 1
        else:
            end = midIndex
    
    return 0


