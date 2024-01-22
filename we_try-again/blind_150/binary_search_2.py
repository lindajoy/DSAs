"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution:
    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # 💡 Helper Function
    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                i = m

            if leftBias:
                r = m - 1
            else:
                l = m + 1
        return i

          
x = Solution()  
print(x.searchRange([5,7,7,8,8,10], 8))

"""
SOMETHING TO REMEMBER:
   Found it while doing this question: https://leetcode.com/problems/length-of-last-word/
   
💡 STR.SPLIT  takes a string and returns a list of substrings of the original string. The behavior differs depending on
   whether the sep argument is provided or omitted.

👉🏾 If sep isn't provided, or is None, then the splitting takes place wherever there is whitespace. 
   However, leading and trailing whitespace is ignored,
   and multiple consecutive whitespace characters are treated the same as a single whitespace character
"""
ten_pm_string = "    fly to the moon  "
print(ten_pm_string.split())