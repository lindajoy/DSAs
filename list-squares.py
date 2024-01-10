"""
Here's the link to exercise:
Squares of sorted array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""
list_1 = [1,2,2,3]

"""
💡 Solution 1: Looping over an iterable 
               Getting the square of each element and then appending it on a list
"""
def _getSquaredNumberOfArray(x):
    funcs = []
    for n in x:
        
        funcs.append(n * n)

    return funcs

print(_getSquaredNumberOfArray(list_1))

"""
💡 Solution 2:  Using the map() function to get the square of each element
"""
def get_square_of_numbers(x):
    return x * x

final_squares = map(get_square_of_numbers, list_1)
print('Using Map Function:',list(final_squares))
        
"""
💡 Solution 3:  Using the List comprehensions to get the square of each element
"""
def get_square_of_list_numbers(x):
    return x * x

final_squares_two  = [get_square_of_list_numbers(i) for i in list_1]
print("Using List Comprehension:", final_squares_two)

names = []
names.append('Joy')
names.append('Miguel')
print('Here are the couples:', names)