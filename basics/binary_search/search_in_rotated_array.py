"""
Now we consider a number of search problems that do not use the binary search principle. 
For example, they focus on tradeofft between RAM and computation time,
avoid wasted comparisons when searching for the minimum and maximum simultaneously, 
use randomization to perform elimination efficiently, use bitJevel manipulations to identify missing elements, etc.
"""
"""

Design an algorithm that takes a 2D sorted array and a number 
and checks whether that number appears in the array.
 For example, if the input is the 2D sorted array, and the number is 7,
your algorithm should retum false; if the number is 8,
your algorithm should return true.
"""

# Here we are using a Binary Search:
# i) By eliminating all the rows and columns that dont contain our target value.

def search_in_2D_array(matrix, x):
    # We start our search in the top right corner
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

matrix = [[1 ,3  ,5],[7,  8,  9], [10 ,12 ,15]]

print(search_in_2D_array(matrix, 16))