# 💡 Arrays BootCamp

# The simplest data structure in a contingous block of memory.
# Usually represents sequences.

"""
Simple question:
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. 
This is easy if you use O(n) space, where n is the length of the array. 
However, you are required to solve it without allocating additional storage.

Sample Input:
Input Array: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

Sample Output:
Reordered Array: [4, 2, 3, 1, 1, 5, 9, 6, 5, 3]
"""
# Whats the input? An array
# Whats the output? An array(even first, then odd)

# 🙃 EASY QUESTION.
# Tume complexity is O(N) => n being the length of the array
# Space complexity is O(1)
def even_odd(A):
    # validate input 
    if not A:
        return []
    
    if len(A) == 1:
        return A
    
    even, odd = 0, len(A) - 1

    while even < odd:
        if A[even] % 2 == 0:
            even += 1
        else:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1
    return A

print(even_odd([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

# 💡 The Dutch National Flag Problem
# Hehe, here we revisit the dreaded quicksort algorithm, Divide and Conquer algorithm.

# Write a program that takes an array A and an index i rnto A, 
# and rearranges the elements such that all elements less than A[r] (the "pivot") appear first, 
# followed by elements equal to the pivot, followed by elements greater than the pivot.

# Suppose array A is equal to A = [0,1,2,0,2,1,1] and the pivot index is 3
# The A[3] = 0, so [0,0,1,2,2,1,1] is valid partioning.
# Mostly Known as the Dutch National Flag
# Where we should return an array that is fully sorted.
# Whenever we are working with the pivot sorting: The one for sure is that we will always be provided with the  pivot index

# Interesting way of assigning variables.
RED, WHITE, BLUE = range(3) 


def dutch_flag_partition(pivot_index, A):
    pivot_element = A[pivot_index]

    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot_element:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot_element:
            break
        for j in reversed(range(i)):
            if A[j] > pivot_element:
                A[i], A[j] = A[j],  A[i]
                break
    return A

print(dutch_flag_partition(3,[0,1,2,0,2,1,1]))

# The above solution, does not sort the array completely.
# But its true to say that its done its job effeciently where all elements that are less
# than the pivot index are on the left

# The above solution however has a time complexity of O(N)^2 and the space complexity is O(1)
# Can we improve it? Yes we can

def dutch_flag_partition_2(pivot_index, A):
    pivot = A[pivot_index]

    # First pass: Group elements smaller than elements
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass:  Group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A

print(dutch_flag_partition_2(3,[0,1,2,0,2,1,1]))
