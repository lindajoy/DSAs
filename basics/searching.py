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

# The time complexity is still O(log n) => This is because each iteration reduces the size of the candidate by half.

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

"""
Design an effecient algorithm that takes a sorted array and a key, and finds the index of the first occurence of an element
greater than than the key. 

For example say that you are given the following array:

[-14, 10, 2, 108, 108, 243, 285, 285, 285, 401]

Our target is 285
The greatest index after 285 is 9
"""
# Whats is the pseudocode of this?

# Initialize the left, right and index(which is what we will return) in the end
# While left <= right:
# We can calculate the mid point: (left +  right) // 2
# if mid_point is equal to target:
#   left = midpoint + 1
# if midpoint > target:
#   index = midpoint
def getIndexOfNextLargestNumber(nums, target):
    left, right = 0, len(nums) - 1, 

    if target not in nums:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return left if left < len(nums) else -1

print(getIndexOfNextLargestNumber([-14, 10, 2, 108, 108, 243, 285, 285, 285, 401], 285))
print(getIndexOfNextLargestNumber([1, 2, 3, 3, 4, 5, 6], 3))
print(getIndexOfNextLargestNumber([1, 2, 2, 3, 4, 4, 5], 2))
print(getIndexOfNextLargestNumber([10, 20, 30, 40, 50], 2))

"""
Write a program which takes a sorted array A integers, and an integer k, and returns the interval enclosing k, i.e,
the pair of integers L and U such that L is the first occurence of k in A and U is the last occurence of k in A.
If k does not appear in A, return [-1,-1]

For example if: A = [1,2,2,4,4,4,7,11,11,13] and k = 11, You should return [7,8]

"""

# 🧐 Here are some of my discoveries.

# We should return an array of pair indexes.
# The thing is this two digits will always "follow each other" in our array.
# So we can let the mid point be our anchor. If we find our target we need to check the index before and after.

# Assumptions:
# Here we will always assume that the the occurence of the number will occur twice in our array.

def searchForAPair(nums, target):
    left, right = 0, len(nums) - 1
    result = [-1, -1]

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            # The two numbers will always follow each other in the other array.
            if mid > 0 and nums[mid - 1] == target:
                result[0] = mid - 1
            else:
                result[0] = mid - 0

            if mid < len(nums) - 1 and nums[mid + 1] == target:
                result[1] = mid + 1
            else:
                result[1] = mid
            return result
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result

print(searchForAPair([1,2,2,4,4,4,7,11,11,13], 11))


