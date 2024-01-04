"""
Minimum Number of Operations to Make Array Empty.

You are given a 0-indexed array nums consisting of positive integers.
There are two types of operations that you can apply on the array any number of times:
    * Choose two elements with equal values and delete them from the array.
    * Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""
"""
Example I:
Input: 
Output: 4
"""
from collections import Counter


nums = [2,3,3,2,2,4,2,3,4]

def minOperations(nums):
    # Initialize an empty dictionary: To Store the occurence of each element.
    nums_count = {}
    # Initialize the number of count operations
    count = 0
 
    for i in nums:
        if i in nums_count:
            nums_count[i] += 1
        else: 
            nums_count[i] = 1

    print('Hello nums count', nums_count)
    for i in nums:
        if nums_count[i] >= 2:
            nums_count[i] -= 2
            count += 1
        if nums_count[i] >= 3:
            nums_count[i] -= 3
            count += 1
        else:
            count += 0
    if all(value == 0 for value in nums_count.values()):
        return count
    else:
        return -1


# print(minOperations(nums))
# print(minOperations([1, 2, 2, 2, 1, 3, 3, 3, 1]))
# print(minOperations([2, 2, 2, 1, 1, 1, 3, 3, 3]))
# print(minOperations([1,2,3,4,5]))

# Interesting Discovery instead of looping through the array and finding
# the number occurences, You can use the counter method
nums3 = [1, 2, 2, 2, 1, 3, 3, 3, 1]
count = Counter(nums3)
print(count)

# DFS Solution.



