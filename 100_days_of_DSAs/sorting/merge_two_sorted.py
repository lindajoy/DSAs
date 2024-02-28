"""

Suppose you are given two sorted arrays of integers. 
If one array has enough empty entries at its end, it can be used to store the combined entries of the two arays in sorted order. 
For example, consider [5,13,17, _, _, _, _ , _] and (3,7,11,19), where _ denotes an empty entry. 
Then the combined sorted entries canbe stored in the first array as [3,5,7,77,73,17,19,_].

Write a Program which takes as input two sorted arrays of integers, 
and updates the first to the combined entries of the two arrays in sorted order. 
Assume the first array has enough empty entries at its end to hold the result.
"""
# Whats the input? Two arrays. First and the second 
# The first array has empty slots towards the end, so we should fill them.

# Hmm lets understand this better:
#   A. [5,13,17, _, _, _, _ , _]
#   B. [3,7,11,19]

# First Iteration:
#   A. [3,5,13,17, _, _, _, _ ]
#   B. [7,11,19]

# Second Iteration:
#   A. [3,5,7,13,17, _, _, _]
#   B. [11,19]

# Third Iteration:
#   A. [3,5,7,11, 13,17, _, _]
#   B. [19]

# Fourth Iteration:
#   A. [3,5,7,11, 13,17, 19, _]
#   B. 

# The Assumption Is the first array has enough empty entries
# Our Output would be something like: [3,5,7,11, 13,17, 19, _]
# Hmm, my loop is not terminating

def mergeTwoSorted(A, B):
    # Assume that the A is the first array , B is the second array.
    ptr_A, ptr_B = 0, 0

    while ptr_A <= len(A)-1 and ptr_B <= len(B) - 1:
        if  A[ptr_A] != '_' and A[ptr_A] > B[ptr_B]:
            # At that particular index it inserts
            A.insert(ptr_A, B[ptr_B])
            # Removes the dash towards the end of the array.
            A.pop()
            ptr_B += 1
            ptr_A += 1
        elif  A[ptr_A] != '_' and A[ptr_A] < B[ptr_B]:
            ptr_A += 1
        elif  A[ptr_A] == '_':
            A.pop()
            A.insert(ptr_A, B[ptr_B])
            ptr_A += 1
            ptr_B += 1


    return A
A = [5,13,17, '_', '_', '_', '_' , '_']
B = [3,7,11,19]
print(mergeTwoSorted(A,B))






