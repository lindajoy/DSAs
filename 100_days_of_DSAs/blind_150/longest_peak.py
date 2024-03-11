"""
💡  LONGEST PEAK

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip 
(the highest value in the peak), 
at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, 
but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. 
Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
"""

# Example 1

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# 6 // 0, 10, 6, 5, -1, -3

# Doing this question, because, I dont like it 🥶

# What are we given? An array
# What is the output? The length of the longest peak.

def longest_peak(arr):
    ans = 0
    i  = 0

    while i + 1 < len(arr):
        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1

        increasing = 0
        decreasing = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            increasing += 1
            i += 1
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            decreasing += 1
            i += 1

        if increasing > 0 and decreasing > 0:
            ans = max(ans, increasing + decreasing + 1)
    return ans

print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
print(longest_peak([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(longest_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(longest_peak([1, 3, 5, 7, 9, 7, 5, 3, 1]))