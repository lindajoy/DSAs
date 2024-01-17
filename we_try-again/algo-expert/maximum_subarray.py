"""
💡 MAXIMUM SUBARRAY

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6


"""

def maxSubArray(nums):
    # Validate the input
    if not nums:
        return 0
    
    # If the array length of the array is equal to 1 ; might as well return it.
    if len(nums) == 1:
        return nums[0]
    
    # Initialize the maximum value.
    max_value = float('-inf')
    left, right = 0, 0
    window_sum = 0

    while right < len(nums):
        window_sum += nums[right]
        right += 1
        max_value = max(max_value, window_sum)

        while left < right and window_sum < 0:
            window_sum -= nums[left]
            left += 1

    return max_value

print('Lemme see:', maxSubArray([-2,-1,-3,]))
print( 5 // 2)
print( -3 / 1)