"""
PRODUCT OF ARRAY EXCEPT SELF

Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
# This is the brute force solution
# The time limit is exceeded 🤔
# But at least I got the slicing right.
def productExceptSelf(nums):
    product_array = []

    for i in range(len(nums)):
        complete_nums = nums[i+1:] + nums[:i]
        produt = 1
        for j in complete_nums:
            produt *= j
        product_array.append(produt)

    return product_array

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# 💡 Better Solution
# This is the O(N) solution.

def productExceptSelf2(nums):
    res = [1] * (len(nums))

    for i in range(1, len(nums)):

        res[i] = res[i-1] * nums[i-1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
print(productExceptSelf2([1,2,3,4]))

