"""
SORTED SQUARED ARRAY.

Write a function that takes in a non-empty array of integers that are sorted in ascending order
and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input: array = [1, 2, 3, 5, 6, 8, 9]
Sample Output: array = [1, 4, 9, 25, 36, 64, 81]
"""
# We forgot if the number is negative.
def sorted_squared_array(arr):
    squared_array = [ i * i for i in arr ]

    # Implemented the bubble sort
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(squared_array) - 1):
            if squared_array[i] > squared_array[i + 1]:
                is_sorted = False
                squared_array[i], squared_array[i + 1] = squared_array[i + 1], squared_array[i]
    return squared_array


print(sorted_squared_array([1, 2, 3, 5, 6, 8, 9]))
print(sorted_squared_array([-4, -2, 0, 1, 3, 5]))