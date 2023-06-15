"""
Link to question = https://www.educative.io/courses/grokking-coding-interview-patterns-python/gkqYr2zPWnr
"""
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

def minutes_to_rot(grid):
    # Count the number of rows and columns
    rows, columns = len(grid), len(grid[0])
    time = 0
    visited = set()

    def dfs(row, column):
        time = 0
        # Base case to check whether the row and columns are within the range of the matrix
        if row < 0 or row >= rows or column < 0 or column >= columns:
            return 0
     
        # Check whether the visited array contains the current row and column that you are on
        if (row,column) in visited:
            return 0
        
        if (grid[row][column] == 0):
            return 0
        
        # Did a stupid mistake did not add the row , column in the visited set.
        visited.add((row, column))  # Add the current cell to the visited set

        # Add the minutes to rot
        time += 1

        dfs(row+1, column)
        dfs(row-1, column)
        dfs(row, column+1)
        dfs(row, column-1)
        time += 1

        return time


    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 2:
                time += dfs(r,c)

    return time


print(minutes_to_rot(grid))