"""
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
Each number was supposed to appear exactly once in the list, however, 
two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. 
Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
"""

"""
EXAMPLE 1

Input: nums = [0,1,1,0]

Output: [0, 1]

The numbers 0 and 1 appear twice in the array
"""
"""
Something Interesting I learnt here:

    1. list.sort(): This is a method of list objects. It sorts the list in place, meaning it
                    directly modified the original list and returns None.

    2. sorted(): Built in function that takes an iterable(list, tuple, string or set) as an argument.
                  Returns a new sorted  list leaving the original iterable unchanged.
"""

def getSneakyNumbers(nums):
    sorted_nums = sorted(nums)
    print(sorted_nums)
    left_ptr, right_ptr = 0, 1
    duplicated_nums = []

    while right_ptr < len(sorted_nums):
        if sorted_nums[left_ptr] == sorted_nums[right_ptr]:
            duplicated_nums.append(sorted_nums[right_ptr])
        left_ptr += 1
        right_ptr += 1

    return duplicated_nums

print(getSneakyNumbers([0,1,1,0]))