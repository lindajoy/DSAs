"""
Inputs : Array, window size.
Output: Maximum number from each window size.
"""

def find_max(arr, w):
    # Remove the edge/easiest cases cases => Which are:
    # 1. length of the array is equal to one => Return the array
    # 2. If the window length is greater or equal to the length of the array return the
    #    return the maximum of the entire array.
    if w >= len(arr):
        return [ max(arr) ]

    if len(arr) == 1:
        return arr

    # Initialize the start and end pointers
    start, end = 0, w
    max_numbers = []

    while end < len(arr):
        end_val = end
        slicedArr = arr[start: end_val - 1]
        
        max_val = max(slicedArr)
        max_numbers.append(max_val)

        # print('Here are my max Numbers', max_numbers)
        start += 1
        end += 1

    return max_numbers

print(find_max([-4, 2, -5, 3, 6], 3))
print(find_max([6], 6))