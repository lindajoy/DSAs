"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), 
at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 2 form a peak, but the integers 1, 2, 4 don't.

Not understood the solution.
"""

def findLongestPeak(array):
    longestPeak = 0
    i = 1

    while i < len(array) - 1:

        isPeak = array[i-1] < array[i] and array[i] > array[i+1]

        if not isPeak:

            i += 1
            continue
        left = i - 2
        right = i + 2

        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        currPeak = right - left - 1

        longestPeak = max(currPeak, longestPeak)

        i = right

    return longestPeak
	
input = [-5, 1, 22, 5, 4, 3, 10]
print(findLongestPeak(input))