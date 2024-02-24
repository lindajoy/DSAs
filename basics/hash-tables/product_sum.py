"""
PRODUCT SUM

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. 
The product sum of a "special" array is the sum of its elements,
where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; 
the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); 
the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).
"""

# INPUT: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# OUTPUT: 12

# def product_sum(arr):
#     total_sum = 0
#     inner_array = 2

#     def calculate_sum(nums):
#         for num in nums:
#             total_sum = 0
#             if isinstance(i, int):
                



#     for i in arr:
#         if isinstance(i, int):
#             total_sum += 1
#         else:
#             calcuate_sum(i)

# print(product_sum( [5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# Output : 12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)

nums_and_nested_lists = [5, 2, [7, -1]]
total_sum = 0
multiplier = 1

# The trouble I am having with this question is with nested lists.
for i in nums_and_nested_lists:
    if isinstance(i, int):
        total_sum += i
    else:
        multiplier += 1
        multiplied_sum = sum(i) * multiplier
        total_sum += multiplied_sum

print(total_sum)        
       

# The problem product sum:
#  => A function that calls itself.
#  => Our input is just a special array.

# This is pretty smart never thought about it this way.
def product_sum(special_array, depth=1):
    # Initialize the total sum to 0
    total_sum = 0
    
    for element in special_array:
        if isinstance(element, list):
            # This function calls itself.
            # This is where the recursion takes place, where we get to 
            # recursively call our function.
            total_sum += product_sum(element, depth + 1)
        else:
            total_sum += element
    # Multiply the total_sum with the depth.
    return total_sum * depth

# Example usage:
special_array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
result = product_sum(special_array)
print(f"Product sum of {special_array}: {result}")