"""
You're given an array of integers and an integer. 
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and 
doesn't need to maintain the order of the other integers.

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
"""

def move_element_to_end(arr, toMove):
    left, right = 0, len(arr) - 1

    while left < len(arr):
        if arr[left] == toMove:
            arr[left],  arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
    return arr

print(move_element_to_end([1,2,3,4,5], 3))
