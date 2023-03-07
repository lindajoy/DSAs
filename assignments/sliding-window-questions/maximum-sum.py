"""
Given an array of positive integers, and a positive number k, 
find the maximum sum of any contiguous subarray of size (k).

💡 Analysis

𐃉 Contiguous means continuous. Meaning that the elements should be next to each other.

𐃉 A subarray is a contiguous sequence of elements within an array.

 ----------FIRST ITERATION----------------

(Working with summation of two integers)

Step  1: We would like to start from the first element of range k and add the next element to it.

K is the size of the subarray.

Input: [3, 5, 2, 1, 7], k=2
Output: 8
Maximum sum = 8
"""
"""
End Goal: Find the sum of a contingous size of the array. (2)

[3,5] => [5,2] => [2,1] => [1,7]
Pseudocode:

Step 1: Start from the the beginning of the array(which is 3)
Step 2: Take the first two elements in the array => 
"""
