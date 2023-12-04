"""
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"""
I struggled on this one maybe I was sleepy.
I think I am a little rusty in Data structures, Need to work harder! 😮‍💨
"""
nums = [1,2,3,4]

# Lets try something
print('What will this output?', nums[2:])
print('At Index 0 what should I expect?', nums[0:])
print('At Index 1 I would like this', print(nums[1:]), print(nums[1+1:]), nums[1:] + nums[1+1:])

# When i slice a list does it take from where I started?
mixed_array = ["Joy", 'Lidah', 'Wawira', 'Joel', 'Justin', 'Mwanzia', 'Anne']
print(mixed_array[1:])
print(mixed_array[3: -1])

# Negative assess of elements in  a list
print('Accessing -4', mixed_array[-4]) # Should print out Joel
print('Accessing -2',mixed_array[-2]) # Should print out Mwanzia

# Hmm🤔 => i need to study more on lists 💡

def findProductOfArrayExceptSelf(nums):
    productArray = []

    for i in range(len(nums)):
        result = nums[:i] +nums[i+1:]
        product = 1

        for i in result:
            product *= i
        productArray.append(product)

    return productArray
       
print(findProductOfArrayExceptSelf(nums))

