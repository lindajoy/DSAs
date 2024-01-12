"""
You're given an array of integers and an integer. 
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

"""

def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1

    while left < right:
        if array[right] == toMove:
            right -= 1

        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]

        left += 1

    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))