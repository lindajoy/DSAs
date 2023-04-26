"""
Given a string, s, that represents a DNA sequence, and a number, k,
return all the contiguous sequences (substrings) of length 
k that occur more than once in the string. 
The order of the returned subsequences does not matter.
If no repeated subsequence is found, the function should return an empty set.

String = "CCATATGTATGGATAT"

Output 1 = "ATAT"
Output 2 = "TATG"
"""

"""
First Solution Pseudocode:
   1. Initialize the seen and repeated  as set() and set()
   2. Initialize the left and right pointers => Start the left with 0, right with k
   3. Loop through the the string while the rightPointer is less than the length of the string
   4. SlicedString(left: right)
   5. Check if the slicedstring exists in seen => If it does add to the repeated else add to the seen.
   6. Increment the left and right pointers by 1.


Question from Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7AWZ9X7ZgJr
"""

def find_repeated_sequences(s, k):

    # First step would be to initialize the seen and repeated sets
    seen , repeated = set(), set()
    
    leftPtr = 0
    rightPtr = k

    while rightPtr < len(s):
        slicedstring = s[leftPtr: rightPtr]

        if slicedstring in seen:
            repeated.add(slicedstring)
        else:
           seen.add(slicedstring)

        
        leftPtr += 1
        rightPtr += 1

    return list(repeated)


"""
Leetcode Version:

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, 
return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
You may return the answer in any order.

Link to question: https://leetcode.com/problems/repeated-dna-sequences/
"""

def find_repeated_sequences(s):

    # First step would be to initialize the seen and repeated sets
    seen , repeated = set(), set()
    
    leftPtr = 0
    rightPtr = 10

    while rightPtr < len(s):
        slicedstring = s[leftPtr: rightPtr]

        if slicedstring in seen:
            repeated.add(slicedstring)
        else:
           seen.add(slicedstring)

        
        leftPtr += 1
        rightPtr += 1

    return list(repeated)