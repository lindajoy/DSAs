"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

def longestConsecutive(nums):
    sorted_nums = sorted(nums)

    left = 0
    right = left + 1
    emptylist = []

    while right < len(sorted_nums):
        if sorted_nums[right] - sorted_nums[left] == 1:
            emptylist.append(sorted_nums[left])

        left = right
        right = right + 1

    return len(emptylist) + 1

nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
print(longestConsecutive(nums2))
