"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
nums = [4,2,7,11,15]
enum_nums = [ (idx, num) for idx, num in enumerate(nums)]
print('Here is my enumerated list:', enum_nums)
sorted_nums = sorted(enum_nums, key= lambda x : x[1])
print('Hello My Sorted Enumerated Numbers', sorted_nums)

def two_sum(nums, target):
    # Enumerating to obtain both the idx, and the number.
    enum_nums = [ (idx, num) for idx, num in enumerate(nums)]
    # Sorting by the numbers instead of the index.
    sorted_nums = sorted(enum_nums, key=lambda x: x[1])
    # Initialize the start and end (Like the MIT professor stated: This is the two finger approach)
    start, end = 0, len(nums) - 1

    while start < len(nums):
        if sorted_nums[start][1] + sorted_nums[end][1] == target:
            return [sorted_nums[start][0], sorted_nums[end][0] ]
        elif sorted_nums[start][1] + sorted_nums[end][1] < target:
            start += 1
        else:
            end -= 1

print(two_sum(nums, 22))

