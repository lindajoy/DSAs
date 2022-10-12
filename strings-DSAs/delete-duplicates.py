'''
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. 

Return the number of valid elements. Many languages have library functions for performing this operation you
cannot use these functions.

Hint:There is an O(n) time and O(1) space solution.

Input: Sorted array
'''

def remove_duplicate_elements(array):
    print(array)
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] == array[j]):
                array.remove(i)
    return array

print(remove_duplicate_elements([2,3,5,5,7,11,11,11,73]))