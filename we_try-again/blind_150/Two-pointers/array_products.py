"""
Write a function that takes in a non-empty array of integers and returns an array of the same length,
where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
"""

array = [5, 1, 4, 2]
output =[8, 40, 10, 20]

# 💡 A reminder on slicing.
print('Sliced at index 1',array[1:])
print('sliced at index 2' ,array[2:]+ array[:1])

def arrayOfProducts(nums):
    n = [0] * len(nums)

    def calc_product(index, list):
        product = 1
        for i in list:
            product *= i
        n[index] = product

    for i in range(len(nums)):
        if i == 0:
            concat_list = nums[1:]
            calc_product(i, concat_list)
        else:
            concat_list2 = nums[i+1:] + nums[:i]
            calc_product(i, concat_list2)
    return n


print(arrayOfProducts(array))
print(arrayOfProducts([1, 2, 0, 4]))
print(arrayOfProducts([-1, 2, -3, 4]))
print(arrayOfProducts([2, -3, 4, -5]))