"""
Understanding the enumerate function in Python list

list = 2,7,11,15
ENUMERATE function allows you to print out indexes and the associated numbers
"""


list_one = [2,7,11, 15]
sample_list = [(nums, idx) for nums, idx in enumerate(list_one)]

print("😁", sample_list)

sample_list2 = [(nums, idx) for idx, nums in enumerate(list_one)]
print('😁❌', sample_list2)