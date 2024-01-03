"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Example 1: 
Input: nums = [5,6,2,7,4]
Output: 34
"""

def maxSumDifference(nums):
    # You never thought about the edge cases
    if not len(nums):
        return 0
    
    sorted_nums = sorted(nums) 
    first_pair = sorted_nums[:2]
    second_pair = sorted_nums[-2:]
    
    product_one = 1
    for nums in first_pair:
        product_one *= nums

    product_two = 1
    for nums in second_pair:
        product_two *= nums

    return product_two - product_one


print(maxSumDifference([5,6,2,7,4]))
print(maxSumDifference([]))