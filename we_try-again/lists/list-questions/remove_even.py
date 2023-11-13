"""
Implement a function that removes all the even elements from a given list.
Name it remove_even(lst)

Input: A list with random integers
Output: A list with odd intergers
"""
my_list = [1,2,4,5,10,6,3]
# output should be my_list = [1,5,3]

# This is a good solution but can be better if we use a list comprehension:
# If you ever find yourself looping through an element to return a value think about list comprehensions instead.

def remove_even(lst):
    odd_numbers = []
    for i in lst:
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

print(remove_even(my_list))

# List comprehension
def remove_even_two(lst):
    return [num for num in lst if num %2 != 0]

print(remove_even_two(my_list))
