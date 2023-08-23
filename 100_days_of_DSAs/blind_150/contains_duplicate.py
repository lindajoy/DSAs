"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: True

Input: nums=  [1,2,3,4]
Output: False

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

🫥 Biggest Mistake: Keep Track of the Variables that you create.

Link to question: https://leetcode.com/problems/contains-duplicate/
"""
nums_array_one = [1,1,1,3,3,4,3,2,4,2]

class Solution:
    def containsDuplicate(self, nums) -> bool:
        sorted_nums = sorted(nums)
        right, left = 0, 1
       
        while left < len(nums):
            if sorted_nums[left] == sorted_nums[right]:
                return True
            right += 1
            left += 1
        return False
