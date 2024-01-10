"""
Given an array of integers between 1 and n, inclusive, where n is the length of the array, 
write a function that returns the first integer that appears more than once (when the array is read from left to right).
In other words, out of all the integers that might occur more than once in the input array, 
your function should return the one whose first duplicate value has the minimum index.
If no integer appears more than once, your function should return -1.
Note that you're allowed to mutate the input array.
"""

def removeFirstDuplicate(array):
    unique_nums = set()

    for i in array:
        if i in unique_nums:
            return i
        else:
            unique_nums.add(i)
    return -1

print(removeFirstDuplicate([2, 1, 3, 4, 3, 2]))
print(removeFirstDuplicate([1, 1, 2, 2, 3, 3]))
print(removeFirstDuplicate([3, 2, 1, 2, 3, 1]))
print(removeFirstDuplicate([2, 1, 5, 2, 3, 3, 4]))
print(removeFirstDuplicate([2, 1, 5, 3, 3, 2, 4]))
print(removeFirstDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3]))


