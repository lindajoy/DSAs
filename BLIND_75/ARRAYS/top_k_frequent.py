"""
TOP K FREQUENT ELEMENTS

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

def top_k_frequent_elements(nums, k):
    frequency_dict = {}

    for i in nums:
        frequency_dict[i] = frequency_dict.get(i, 0) + 1

    sorted_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse= True)

    return [i[0] for i in sorted_dict ][:k]

print(top_k_frequent_elements([1,1,1,2,2,3],2))