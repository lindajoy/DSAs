"""
ARRAY OF PRODUCTS.

Write a function that takes in a non-empty array of integers and returns an array of the same length, 
where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

"""

# SAMPLE INPUT: array = [5, 1, 4, 2]

# [8, 40, 10, 20]
# // 8 is equal to 1 x 4 x 2
# // 40 is equal to 5 x 4 x 2
# // 10 is equal to 5 x 1 x 2
# // 20 is equal to 5 x 1 x 4


# Lets remind ourselves on slicing:
array = [5, 1, 4, 2]

print(array[1:])
print(array[:0])

def product_of_array(nums):
    res = []

    def calculate_product(arr):
        product = 1
        for i in arr:
            product *= i
        return product

    for i in range(len(nums)):
        sliced_array = nums[i+1:] + nums[:i]
        prod = calculate_product(sliced_array)
        res.append(prod)

    return res

print(product_of_array([5, 1, 4, 2]))

    



