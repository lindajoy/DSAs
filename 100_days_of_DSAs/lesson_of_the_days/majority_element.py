"""
💡 MAJORITY ELEMENT.

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Sample:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# Whats the input? An array of elements
# Whats the output? Majority element.

# Approach: Use Hash map to keep count of each element.

def majority_element(nums):
    count_dict = {}

    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    count_dict_sorted = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    return count_dict_sorted[0][0]

print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([3,2,3]))