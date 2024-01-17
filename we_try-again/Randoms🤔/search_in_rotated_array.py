"""
💡 Search in Rotated Sorted Array.

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

# This is an explanation step by step approach of the question above
# Example 1
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output = 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

def searchInRotatedArray(nums, target):
    # Initialize the left and the right pointers
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        # If you are lucky the number in the middle is equal to the target; return its index
        if nums[mid] == target:
            return mid  
        # Check if left half is sorted.
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(searchInRotatedArray([4,5,6,7,0,1,2], 0))
        


