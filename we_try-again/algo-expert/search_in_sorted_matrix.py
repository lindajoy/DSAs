"""
You're given a two-dimensional array (a matrix) of distinct integers and a target integer. 
Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1].
matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
          ]
target = 44

Answer should be: [3,3]
"""
matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
          ]
target = 44

# This time complexity is 0(m * n )

# How can we minimize that? 🤔
def searchInSortedMatrix(matrix, target):
    rows, colums = len(matrix), len(matrix[0])
    for r in range(rows):
        for  c in range(colums):
            if matrix[r][c] == target:
                return [r,c]
            
print(searchInSortedMatrix(matrix, target))

# Using Binary Search
def search_in_matrix(matrix, target):
    # Validate the input
    if not matrix or not matrix[0]:
        return [-1, -1]

    # We get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return [-1, -1]

print(search_in_matrix(matrix, target))  

