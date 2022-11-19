'''
Given an integer array and a window of size w, find the current maximum value in 
the window as it slides through the entire array.

💡 Note: If the window size is greater than the array size, we consider the entire array as a single window.


(inputs) => integer array, window size
(output) => maximum number in the sliding window.
'''


def findmaxNumberInSlidingWindow(array: list[int], window_size: int) -> list[int]:
    # First check whether window size id greater than the array_size and return its max value.

    if window_size > len(array):
        return max(array)

    # Next, we loop through the contingous array to find the max number for each contigous subarray

    left = 0
    max_value = 0

    for i in range(len(array)):
        while left > len(array) - 1:
            _loopedarray = array.slice[left, window_size - 1]
            print(_loopedarray)
            max_value = max(_loopedarray)
            left += 1
            return max_value
    return max_value       

nums = [-4, 5, 4, -4, 4 , 6, 7]
window = 2

print(findmaxNumberInSlidingWindow(nums, window))
