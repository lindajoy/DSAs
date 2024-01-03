"""
You are given an integer array nums. 
You need to create a 2D array from nums satisfying the following conditions:

=> The 2D array should contain only the elements of the array nums.
=> Each row in the 2D array contains distinct integers.
=> The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.
Note that the 2D array can have a different number of elements on each row.
"""

def findMatrix(nums):
    two_array = []

    set_list = set(nums)

    # if len(nums) == len(set_list):
    #     two_array.append(nums)

    while len(nums) > 0:
        set_two = set(nums)
        if (len(set_two) != 0):
           two_array.append(list(set_two))

        for i in set_two:
            nums.remove(i)
            print(nums)


    return two_array

print(findMatrix([2,3,1]))
