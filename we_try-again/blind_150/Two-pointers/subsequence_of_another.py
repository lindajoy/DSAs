"""
Given two non-empty arrays of integers, 
our goal is to write a function that establishes whether the second array is a valid subsequence of the first array.
A valid subsequence of an array is classified as a set of numbers that aren’t necessarily adjacent in the array but are in the same order as they appear in the array. 
For example, [2, 5, 6] and [2, 6] are both considered as valid subsequences of the array [2, 3, 4, 5, 6]. 
It is also important to note that [2] and [2, 3, 4, 5, 6] are both valid subsequences of the array.

Sample:

Input array → [3, 6, 23, 7, 2, 4]

Sequence → [3, 7, 4]

Output → True
"""

# For Loop: Takes O(n) time; n being the length of the array + sequence
# Space complexity: We are storing the set_ptr which takes O(1)
def isValidSubsequence(array, sequence):
    seq_ptr = 0
    for i in range(len(array)):
        if seq_ptr == len(sequence):
            break
        if sequence[seq_ptr] == array[i]:
            seq_ptr += 1

    return seq_ptr  == len(sequence)
     
array1 = [3, 6, 23, 7, 2, 4]
Sequence1 = [3, 7, 4]
array2 = [1, 2, 3, 4, 5]
Sequence2 =[1, 3, 5]
array3= [10, 20, 30, 40, 50]
Sequence4 = [20, 40]
print(isValidSubsequence(array3, Sequence4))
