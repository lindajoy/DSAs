"""
Binary search is a searching algorithm for finding an element's
position in a sorted array.
The element is always searched in the middle of a portion of an array

Binary Search Algorithm can be implemented by:
1. Iterative method
2. Recursive method

The recursive method follows the divide and conquer approach
"""

# Iterative method
def binarySearch(array, x, low, high):
    # Repeat until the pointer low and high meet each other
    while low <= high:
        mid = (low + high)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)
print(result)

# Binary Search (Recurive)
def binarySearch_Recurive(array, x, low, high):
    if high >= low:
        mid = low + (high -low)//2

        #If found at mid, then return it
        if array[mid] == x:
            return mid
        
        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        
        # search the right half
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1