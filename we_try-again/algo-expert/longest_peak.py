"""
The Longest Peak problem involves finding the length of the longest subarray that represents a "peak" within a given array.
A peak is defined as a sequence of at least three integers that satisfies the following conditions:

1. It starts with a sequence of strictly increasing integers.
2. It reaches a peak (an element where it's strictly greater than its adjacent elements).
3. It ends with a sequence of strictly decreasing integers.

The task is to identify these peaks within the array and determine the length of the longest one.

Here's a breakdown of the problem:

- Input: An array of integers.
- Output: The length of the longest peak in the array.

For instance, given an array `[1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]`, 
the longest peak is `[1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]`, and its length is `11`.
This peak starts with `1`, rises to `9`, and then decreases back to `5`.

The task usually involves iterating through the array elements while keeping track of the increasing and decreasing sequences to identify peaks and calculate their lengths.
"""

def longest_peak(array):
    n = len(array)
    max_length = 0

    # Initialize the i index to 1
    i = 1
    while i < n - 1:
        # Check for peak
        is_peak = array[i - 1] < array[i] > array[i + 1]

        if not is_peak:
            i += 1
            continue

        # Expand to left
        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        # Expand to right
        right = i + 2
        while right < n and array[right] < array[right - 1]:
            right += 1

        current_lenght = right - left  - 1
        max_length = max(max_length, current_lenght)
        i = right
    return max_length

print(longest_peak([1,  2]))
            
