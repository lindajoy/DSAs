"""
Given an array of integers arr and an integer k. 
Find the least number of unique integers after removing exactly k elements.

Say you had:
arr = [5,5,4] k = 1
You can remove 4 so that the length of unique integers is one

Example 2:
arr = [4,3,1,1,3,3,2], k = 3

Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
"""

# Brute Force Approach would be:
#   1. Create a dictionary count_dict and store the count of each character in the array and sort them
#   2. Loop the array while the k is greater than 0, decrement the value of k while we loop through the array.
#   3. lastly filter out the values that are greater than 0
#   4. Return the length of x.

def leastNumberOfUniqueIntegers(arr, k):
    # Create a dictionary to store the count of each element
    count_dict = {}

    for i in arr:
        count_dict[i] = count_dict.get(i, 0) + 1

    count_dict = sorted(count_dict.values())

    for i in range(len(count_dict)):
        if k > 0 and count_dict[i] > 0:
            # Mistyped this part
            count_dict[i], k = count_dict[i] - k, k - count_dict[i]


    x = [i for i in count_dict if i > 0]
    return len(x)

print(leastNumberOfUniqueIntegers([4,3,1,1,3,3,2], 3))

# 💡 Using a heap;

# Lets talk about heaps kidogo..

"""
A heap is a specialized binary tree. 

We use heaps when all we care about is the largest or the smallest elements , and you do not need to support fast lookcup, delete , 
or search oparations for arbitary elements.

A heap is good choice when you need to compute the k largest or k smallest in a collection

"""

import heapq
from collections import Counter

def return_unique_elements_from_array(arr, k):
    # Here we are creating a dictionary with a counter that counts every account;
    # and store them in a dictionary
    count_dict = Counter(arr)
    # Converts the freq_list to a list
    freq_list = list(count_dict.values())
    # Here we are converting our list to a heap
    heapq.heapify(freq_list)

    # We use len of heap to help us output the end result
    res = len(freq_list)

    while k > 0 and freq_list:
        # Pops out the smallest element.
        value = heapq.heappop(freq_list)
        if k >= value:
            k = k - value
            res -= 1

    return res
print(return_unique_elements_from_array([4,3,1,1,3,3,2], 3))
