"""
💡 TOP K FREQUENT ELEMENTS

Given an integer array nums and an integer k, return the most k frquent elemnts. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
def topKFrequent(nums, k):
    nums_dict = {}

    for i in nums:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1
    
    output = []
    # list_nums = all(values == k for values in nums_dict.values()) 
    list_nums = [(key, value) for key, value in nums_dict.items() if value == k]

    for i, occ in list_nums:
        return output.append(i)
    return output

print(topKFrequent([1,1,1,2,2,3], 3))