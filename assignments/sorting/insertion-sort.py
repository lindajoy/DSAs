"""
Insertion Sort
"""

# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space

def insertionSort(A):
    for i in range(len(A)- 1):
        nxt = i + 1
        curr = i

        #comparisons like the bubble sort
        while curr >=0 and A[curr] > A[nxt]:
            A[curr], A[nxt] = A[nxt] , A[curr] #swap

            curr -= 1
            nxt -= 1
    return A

unsorted_arry2 = [0, 1,2,0,2,1,1]
sorted_array2 = insertionSort(unsorted_arry2)
print(sorted_array2)

"""
💡 Second Solution

   Divide the input array into two subarrays in place
   The first subarray should be sorted at all times  and should start with a length of 1 
   while the second subarray should be unsorted.

   Iterate through the unsorted subarray, inserting all of its elements into the sorted subarray in the correct position
   by swapping them into place.

   Eventually, the entire array will be sorted.
"""


def insertionSort00(array):
    for i in range(1 , len(array)):
        # add a new element(array[i]) to the sorted array
        # the sorted array will now end at i

        added = i
        while array[added] < array[added - 1]:
            # swap
            array[added], array[added -1] = array[added - 1], array[added]
            added -= 1

    return array

unsorted_array = [0, 1, 2, 5 ,3 ,2, 1]
sorted_array = insertionSort(unsorted_array)
print(sorted_array)
