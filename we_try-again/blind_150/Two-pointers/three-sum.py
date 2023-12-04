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
numsm = [-1,0,1,2,-1,-4]
my_list_two = [-1,0,1,0]
'''
Wrong Answer => Does not return distinct triplets array; Its repetitive.
'''
def sum_of_three(nums):
    distinct_triplets = set()
    sorted_array = sorted(nums)
    right = 0
    next_to_right = right + 1
    left = len(nums) - 1

    while right < left:
        if sorted_array[right] + sorted_array[left] + sorted_array[next_to_right] == 0:
            distinct_triplets.add((sorted_array[right], sorted_array[left] ,sorted_array[next_to_right]))
            right += 1
            next_to_right += 1
            left -= 1
        elif sorted_array[right] + sorted_array[left] + sorted_array[next_to_right] > 0:
            left -= 1
        else:
            right += 1
            next_to_right += 1

    return set(distinct_triplets)

# print(sum_of_three(my_triplet_list))
# print(sum_of_three(numsm))
# print(sum_of_three(my_list_two))

'''
Wrong  Answer => Again; Analysis and fix what did not work in the previous code
'''

def sum_of_three_improved(nums):
    distinct_triplets = set()
    sorted_array = sorted(nums)

    for i in range(len(sorted_array) - 2):
        print("The value of I at this particular point", i)
        if i > 0 and sorted_array[i] == sorted[i - 1]:
            continue

        left, right = i + 1, len(sorted_array) - 1

        while left < right:
            total = sorted_array[i] + sorted_array[left] + sorted_array[right]

            if total == 0:
                distinct_triplets.add((sorted_array[i], sorted_array[left],sorted_array[right]))

                # skip duplicate to avoid duplicate triplets
                while left < right and sorted_array[left] == sorted_array[left + 1]:
                    left += 1
                while left < right and sorted_array[right] == sorted_array[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

        return distinct_triplets
    
# print(sum_of_three_improved(my_triplet_list))
# print(sum_of_three_improved(numsm))


# Let try again:

def threeSum(nums):
    res = set()
    sorted_nums = sorted(nums)
    print(sorted_nums)

    for i , a in enumerate(sorted_nums):
       # Enumerate generates index, and the value(belonging to that index)
       if i > 0 and a == [i - 1]:
           
           continue
       
       left, right = i + 1, len(sorted_nums) - 1

       while left < right:
           potentialSum = a + sorted_nums[left] + sorted_nums[right]

           if potentialSum > 0:
               right -= 1
           elif potentialSum < 0:
               left += 1
           else:
               res.add((a, sorted_nums[left] ,sorted_nums[right]))
               left += 1
               while sorted_nums[left] == nums[left - 1] and left < right:
                   left += 1
    return res

print(threeSum(numsm))
print(threeSum([-1,0,1,0]))