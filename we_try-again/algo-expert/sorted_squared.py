"""
Sorted Squared Array
Given an array of integers that are sorted in increasing order, 
Write a function that squares all the integers
in the array and returns them in a new array, also sorted in increasing order.
"""

# 💡 For this operation we use a bubble sort.

# 💡 Example
# Input: [-4, -2, 0, 3, 5]
# Output: [0, 4, 9, 16, 25]
nums = [-4, -2, 0, 3, 5]
def sorted_squared_array(nums):
    # Here is what the operation should do...Returns the squares.
    squares = [(i**2) for i in nums]

    # Here I am using the bubble sort
    # n = len(squares)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         print(f"What is the value of j?{j}")
    #         if squares[j] > squares[j+1]:
    #             squares[j], squares[j+1] = squares[j+1], squares[j]
    # return squares
    # Get the length of the squares
    len_squares = len(squares) - 1
    for i in range(0, len_squares):
        if squares[i] > squares[i + 1]:
            squares[i], squares[i + 1] = squares[i+1], squares[i]

    len_squares -= 1
    return squares

print(sorted_squared_array(nums))

"""
This actually makes more sense
"""

# 💡 Important lesson learnt an this chanllenge or a reminder rather:

def bubbleSort(lst):
    end = len(lst) - 1

    while end > 0:
        for i in range(0, end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        end -= 1
    return lst

print(bubbleSort([5,2,1,0,8,1]))