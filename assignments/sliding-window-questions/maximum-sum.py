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
# What are the inputs? An array and k the size of the subarray
# Time Complexity for this algorithm is O(N); n being the length of the array.

def maximum_sum(lst, k):
    max_entry = float("-inf")

    for i in range(len(lst)):
        next_index = i + k
        if next_index < len(lst):
            sum_of_list = sum(lst[i: i+k])
            max_entry = max(max_entry, sum_of_list)

    return max_entry

print(maximum_sum([3, 5, 2, 1, 7], 2))
print(maximum_sum([4, 2, 1, 7, 8, 3], 3))
print(maximum_sum([1, 3, 5, 2, 9, 7, 4], 2))
  