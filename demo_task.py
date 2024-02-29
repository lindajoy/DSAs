"""
Write a function:

def solution(A):

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# PERSONAL NOTE

# @joy I like this question because I like the word effecient where it says write an effecient algorithm.

# What makes an effecient algorithm?

#   1. Correctness => An algorithm must be correct it should output the correct output no matter the size of the input.
#   2. Resource Consumption => An effecient algorithm minimizes execution time and effecient algorithms also use minimal space.

def solution(A):
    # We are minimizing the size of our input
    A = [i for i in A if i > 0]
    
    # If our array is empty
    if not A:
        return 1
    
    # lets remove duplicates
    A = set(A)
    A = sorted(A)

    smallest_integer = 1

    for i in A:
        if smallest_integer == i:
            smallest_integer += 1
        else:
            return smallest_integer
    return smallest_integer
