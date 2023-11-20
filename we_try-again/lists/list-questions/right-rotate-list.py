"""
This should be reviewed:

Implement a function right_rotate(lst, k) which will rotate the given list by k. 
This means that the right-most elements will appear at the left-most position in the list and so on. 
You only have to rotate the list by one element at a time.

Input: [10,20,30,40,50]
k = 3
Sample Output: [30,40,50,10,20]
"""

"""
🤔 Question for interviewer: 
1. What if k is greater than the length of the list?
2. Will the list contain strings/integers?
3. Is it possible that we have or encounter an empty list as our input?

Ask a clarifying question.

So example: Given this input: [10,20,30,40,50]
k = 1

Shoud our output be: [20,30,40,50,10] ?

A good question to look at: https://leetcode.com/problems/search-in-rotated-sorted-array/ 
Binary Search Question.

"""
x = [10,20,30,40,50]
k = 3

def right_rotate(lst, k):
    if len(lst) == 0: 
        k = 0
    else:
        k = k%len(lst)
        print('Here is the value of k', k)

    # Initialize the rotated list
    rotatedList = []

    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        print('1st Loop, Item',item)
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        print('2nd Loop, Item',item)
        rotatedList.append(lst[item])
    return rotatedList

print(right_rotate(x, k))

"""
💡 Second solution
"""

def rotate_array(nums, k):
    rotated = [0] * len(nums)

    for i in range(len(nums)):
        new_index = (i + k) % len(nums)
        rotated[new_index] = nums[i]
    return rotated

# Tested with the case where the length of the array is less than k.
print(rotate_array([1,2,3],7))