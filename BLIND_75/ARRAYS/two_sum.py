"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def two_sum(arr, target):
    enumerated_arr = [(idx, num) for idx, num in enumerate(arr)]
    left, right = 0, len(enumerated_arr) - 1

    while left < right:
        if enumerated_arr[left][1] +  enumerated_arr[right][1] == target:
            return [enumerated_arr[left][0],  enumerated_arr[right][0]]
        elif enumerated_arr[left][1] +  enumerated_arr[right][1] > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]


print(two_sum([2,7,11,15], 9))