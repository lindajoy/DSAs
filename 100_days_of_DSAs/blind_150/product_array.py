"""
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Sample Example of input and output:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"""
Remind myself some of lists manipulations
"""

nums = [1, 2, 3, 4]
# One is the actual index in the array while 2: are the numbers after 2:
# result = nums[:1] + nums[2:]
# print(nums[:1])
# print(nums[2:])
# print(result)

"""
This is not the optimal solution since we have two for loops so most likely its a quadractic(On2) solution.
"""
def product_of_array_except_self(nums):
    product_array = []
    for i in range(len(nums)):
        result = nums[:i] + nums[i+1:]
        product = 1

        for i in result:
            product *= i
        product_array.append(product)

    return product_array


