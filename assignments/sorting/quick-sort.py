"""
💡 Quick SORT
    The quicksort algorithm for sorting arrays proceeds recursively-it selects an element (the "pivot"),
    reorders the array to make all the elements less than or equal to the pivot appear first, followed by
    all the elements greater than the pivot. The two subarrays are then sorted recursively

    It kinda follows the divide and conquer approach.

    For this: I used the Dutch National Flag Problem (see EOP)
"""

def ducth_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    # First pass: group of elements smaller than the pivot
    for i in range(len(A)):
        #look for a smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A [j], A[i]
                break

    # Second Pass: Group of elements larger than the pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element.Stop when we reach an element less than
        # pivot , since first pass has to moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j] , A[i]
            break
    return A

unsorted_arry = [0, 1,2,0,2,1,1]
sorted_array = ducth_flag_partition(2, unsorted_arry)
print(sorted_array)

# Second Solution

def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i] , A[smaller] = A[smaller], A[i]
            smaller += 1

    #