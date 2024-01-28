"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
                2 is the missing number in the range since it does not appear in nums.
"""

# Input: Array of numbers
# Output: Missing Number

# Question for the interviewer
#
# 1. Is it possible to get an empty array, or we can assume our list of numbers will always have something?
# 2. Our array will always contain positive numbers right? 🙃

# The time complexity here would be O(n); n being the lenght of the array.

def missing_number(nums):
    # Validate the input
    for i in range(len(nums) + 1):
        if i not in nums:
            return i

print(missing_number([9,6,4,2,3,5,7,0,1]))