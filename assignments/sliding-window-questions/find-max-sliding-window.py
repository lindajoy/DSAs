'''
Given an integer array and a window of size w, find the current maximum value in 
the window as it slides through the entire array.

💡 Note: If the window size is greater than the array size, we consider the entire array as a single window.


(inputs) => integer array, window size
(output) => maximum number in the sliding window.

❌🤥 Personal Analysis: Poorly Done Question => Needs To Be redone
'''

# First attempt(Passed 1 Condition) => Terrible solution

from collections import deque


def findmaxNumberInSlidingWindow(array: list[int], window_size: int) -> list[int]:
    # First check whether window size id greater than the array_size and return its max value.
    if window_size > len(array):
        return max(array)

    # Next, we loop through the contingous array to find the max number for each contigous subarray
    left = 0
    max_nums = []

    for i in range(len(array)):
        while i >=  len(array):
            x  =  array.slice[left, window_size-1]
            print('Heres X:', x)
            left += 1
            max_nums.push(max(x))
            return max_nums
    return max_nums
       
       

nums = [-4, 5, 4, -4, 4 , 6, 7]
window = 2

# print(findmaxNumberInSlidingWindow(nums, window))


'''
Solution 2 (Had to read to find this solution and understand deques)
'''

def find_max_sliding_window(nums, window_size):
    result = []
 
    # Initializing a double ended queue for storing indices
    window_size = deque()

    # Returns 0 if nums is empty
    if len(nums) == 0:
        return result

    # If window_size is greater than the array size,
    # set the window_size to the array size
    # Why not Just check the maximum value in the array if the window size is greater than the length
    # if window_size > len(nums):
    #     window_size = len(nums)


    # Find out the maximum value in the window
    for i in range(window_size):
        print(f"\tIteration {i+1}. Window: {window}")
        # For every element, remove the previous smaller elements from window
        while window and nums[i] >= nums[window[i]]:
            print(f"\t\tnums[{i}] = {nums[i]} is greater than or equal to nums[window[-1]] = {nums[window[-1]]}")
            window.pop()
            print("\t\tWindow after popping:", window)

        # Add current element at the back of the queue
        window.append(i)

    # Appending the largest element in the window to the result
    result.append(nums[window[0]])

    return result

print(find_max_sliding_window(nums, 3))



