"""
Given a 2D array(m x n). 
The task is to check if there is any path from top left to bottom right. 
In the matrix, -1 is considered as blockage (can’t go through this cell) and 0 is considered path cell (can go through it).

Note: Top left cell always contains 0

Example: arr[][] =
{{ 0, 0, 0, -1, 0}, 
{-1, 0, 0, -1, -1}, 
{ 0, 0, 0, -1, 0}, 
{-1, 0, 0, 0, 0}, 
{ 0, 0, -1, 0, 0}} 

Return for this one a path exists

Pseudocode:
1. Find the length of both the rows and columns
2. Create a dfs function that will loop through the entire matrix
3. Check for the base case first
4. On the dfs function, the base case is to check whether the we are out of bounds
5. Mark the cell as visited
6. Check whether we are at the bottom left index return True.
"""

# Returns a True or Falsy value incase a path exists.

def doesPathExist(matrix):
    rows, columns = len(matrix), len(matrix[0])
    directions = [ (1,0), (-1,0), (0, 1), (0,-1)]
    starting_point = [0, 0]
    ending_point = [4, 4]


    def dfs(row, column):
        if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[0]):
            return False
        
        if [row, column] == ending_point:
            return True
        
        # Mark current index as visited
        matrix[row][column] = -1

        if matrix[row][column] == [rows - 1][columns -1]:
            return True
        
        for dr, dc in directions:
            row, column = dr + row , dc + column
            dfs(row, column)

    return dfs(starting_point[0],starting_point[0])