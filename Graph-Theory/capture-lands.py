"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

def captureRegions(matrix):
    # Get the number of rows and columns
    rows, columns = len(matrix), len(matrix[0])

    # Capture the Unsurrounded region
    def capture(row, column):
        # Base Case is to check whether the row and column are within the matrixes range
        if row < 0 or column < 0 or row == rows or column == columns or matrix[row][column] == "X":
            return
        
        # Also marks this as visited
        matrix[row][column] = "T"
        capture(row + 1, column)
        capture(row - 1, column)
        capture(row, column - 1)
        capture(row, column + 1)

    # capture the surrounded region
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "0":
                matrix[r][c] = "X"

    # Capture the unsurrounded region
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "T":
                matrix[r][c] = "0"

    