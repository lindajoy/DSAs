"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
"""
Can you append a list on another list? 🧐
"""
# Interestingly you can append a list on another list 🧐
my_big_list = []
my_random_list = ["Joy", "Linda", "Wawi", "Imani"]
my_big_list.append(my_random_list)
print('Here is my big list: ',my_big_list)
my_other_list = ["Ann", "Rita", "Mwenda"]
my_big_list.append(my_other_list)
print('I have added another list', my_big_list)

my_triplet_list = [0,0,0,0,0,0]

def sum_of_three(nums):
    distinct_triplets = []
    sorted_array = sorted(nums)
    right = 0
    next_to_right = right + 1
    left = len(nums) - 1

    while right < left:
        if sorted_array[right] + sorted_array[left] + sorted_array[next_to_right] == 0:
            distinct_triplets.append([sorted_array[right], sorted_array[left] ,sorted_array[next_to_right]])
            right += 1
            next_to_right += 1
            left -= 1
        elif sorted_array[right] + sorted_array[left] + sorted_array[next_to_right] > 0:
            left -= 1
        else:
            right += 1
            next_to_right += 1

    return distinct_triplets

print(sum_of_three(my_triplet_list))