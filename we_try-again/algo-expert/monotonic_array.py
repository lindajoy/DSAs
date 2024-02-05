"""
Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; t
hey simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

# Example one
Input:[1, 2, 3, 4, 5]
Output: True

# Example Two
Input: [5, 4, 3, 2, 1]
Output: True

Example 3
Input: [1, 3, 2, 5, 4]
Output: False

Example 4 

Input: [2,2,3,4,5]
Ouput: True

"""
# What is the input? An array
# What is the output? Boolean

# Time complexity is O(n); n being the length of the numbers
# Space complexity is O(1) 

def isMonotonicArray(nums):
    isDecreasing, IsIncreasing = False, False
    left, right = range(2)

    while right < len(nums) - 1:
        if nums[left] < nums[right]:
            IsIncreasing = True
        elif nums[left] > nums[right]:
            isDecreasing = True
 
        if isDecreasing and nums[right] > nums[left]:
            return False
        elif IsIncreasing and nums[right] < nums[left]:
            return False
        
        right += 1
        left += 1
    return True

    
print(isMonotonicArray([1, 3, 2, 5, 4]))
print(isMonotonicArray([1, 1, 1, 1, 1]))
print(isMonotonicArray([5, 4, 3, 3, 2, 2, 1]))
print(isMonotonicArray([5, 3, 2, 4, 1]))
print(isMonotonicArray([[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]]))

    
    