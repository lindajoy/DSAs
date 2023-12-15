# Selection Sort 

"""
Selection sort is conceptually the most simplest sorting algorithm. 
This algorithm will first find the smallest element in the array and swap it with the element in the first position, 
then it will find the second smallest element and swap it with the element in the second position, 
and it will keep on doing this until the entire array is sorted.

It is called selection sort because it repeatedly selects the next-smallest element and swaps it into the right place.
"""

def selection_sort(arr):
    len_of_array = len(arr)

    for i in range(len_of_array):
        # We assume the minimum index starts at index 0
        min_idx = i
        # Loop through the array from index (i + 1, and length of array)
        for j in range(i+1, len_of_array):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))


        