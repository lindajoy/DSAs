"""
Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.
"""

def isMonotonicArray(arr):
    isDecreasing = isIncreasing = False

    if arr[0] < arr[1]:
        isIncreasing = True
    elif arr[0] > arr[1]:
        isDecreasing = True
    else:
        return False

    for i in range(len(arr) - 1):
       if isIncreasing and arr[i + 1] < arr[i]:
            return False
       elif isDecreasing and arr[i + 1] > arr[i]:
            return False
       
    return True

# This is increasing        
print(isMonotonicArray([1, 2, 3, 4, 5]))
# This is the same
print(isMonotonicArray([2, 2, 2, 2]))
# This is decreasing
print(isMonotonicArray([9, 8, 7, 6, 5, 4]))
