"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

def contains_duplicate(nums):
    unique_numbers = set()

    for i in nums:
        if i in unique_numbers:
            return True
        else:
            unique_numbers.add(i)
    return False
        

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

