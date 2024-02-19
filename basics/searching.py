"""
February 18th, 2024
"""

# Binary Search.

# Question

"""
Given an arbitary collection of n keys, the only way to determine if a search key is present is by examining
each element. This has O(n) time complexity.

Fundamentally, binary search is a natural elimination-based strategy for searching a sorted array.
The idea is to eliminate half the keys from consideration by keeping the keys in sorted order. 
If the search key is not equal to the middle element of the array,  one of the two sets of kesy to the left and to the right of the middle elemnt can be
eliminated from further consideration.

Question based on binary search are ideal from the interviewers perspective:
        => It is a basic technique that every reasonable candidate is supposed to know and it can be implemetated in a few lines of code.
        => Binary search is much trickier to implement correctly than it appears - you should implement it as well as write corner case tests to ensure you understand it properly.
"""

# What makes Binary Search an impresssive algorithm?
# It executes in O(log n) time

def bsearch(target, arr):
    Left, Right = 0, len(arr) - 1

    while Left <= Right:
        # The error is in the assignment M = ( (Left + Right) // 2) which could potentially lead to an overflow.
        # The overflow can be avoided by using M = L + (U - L) / 2
        # Hmm not sure I agree with this.
        M = (Left + Right) // 2

        if arr[M] == target:
            return M
        elif arr[M] > target:
            Right = M - 1
        else:
            Left = M + 1
    return -1

# Search A Sorted Array for the first occurence of k
"""
Write a method that takes a sorted array and a key and retums the index of the first occurrence
of that key in the array. Retum -1 if the key does not appear in the array. For example, 
when applied to the array in your 
algorithm should return 3 if the given key is 108; if it is 285, 
your algorithm should retum 6.
"""

# A question that should come to  mind?

# What happend when every entry equals k? Dont stop when you see first k

# If K is not found in the array, return -1

array_example = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# A naive approach would be looping through each element from left to right, 
# We will always find the first element in the array.
# This would take O(n) time, but consider when we have a large array of 100000 records this means that
# the algorithm will execute with O(10000)

# BINARY SEARCH WAY

# The binary search takes time O(n log n), where n is the number of entries in the array.
# Traversing backwards takes O(n) time in the worst case  - consider the case where entries are equal to k

# The fundamental idea of binary search is to maintain a set of candidate solutions.
# For the current problem, if we see the element at index i equals k, although we do not know whether i is the first element equal to k
# we do know that no subsequent elements can be the first one.
# Therefore we remove all elements with index i + 1 or more from the candidates

def search_first_of_k(A, k):
    # Initialize the left and the right pointers.
    left, right, result = 0, len(A) - 1, -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
        else:
            result = mid 
            right = mid - 1
    return result

print('First instance of 2', search_first_of_k([2,2,2,2,2,2], 2))
print('First Instance of 300', search_first_of_k([297,298, 299,299,299,300,301,302,303,304,305], 300))
