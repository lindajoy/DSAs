"""
You are given an increasing-decreasing array and asked to sort it

Say you had the following array: 57,131,493,294,221,339,418,452,442,190
The output could be something like: 57,131,190,221,294,339,418, 442,452
"""

def sort_increasing_decreasing_array(A):
    # Decomposes A into a set of sorted arrays
    sorted_subarrays = []
    # This ouputs 0,1
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0

    for i in range(1, len(A) + 1):
        if (i == len(A) or
            (A[i - 1] < A[i] and subarray_type == DECREASING) or
            (A[i - 1] >= A[i] and subarray_type == INCREASING)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type == INCREASING else A[i - 1: start_idx - 1: -1]) 

            start_idx = i
            subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)

    retrun
