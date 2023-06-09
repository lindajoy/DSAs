"""
You are given a two dimensional array(a matrix) of potentially unequal height of width containing only 0s and 1s.
Each 0 represents land and each I represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent(but not diagonally adjacent).
The number of adjacent 1s forming a river determine its size.

Note that the river can twist. In other words, it does not have to be a straight vertical line or straight horizontal line; It can be L-shaped, for example.

Write a function that returns an array of sizes of all rivers represented in the input matrix. The sizes dont need to be any particular order.

grid = [[0, 1, 0, 1, 0],[1, 0, 1, 0, 1],[0, 1, 0, 1, 0],[1, 0, 1, 0, 1]]
"""

"""
In this question we will use a popular graph traversal method called Depth First Search.
Pseudocode:
 1. Initialize the number of rows and columns
 2. Loop through the entire matrix, Check if there are any 1s, if the position you are on has a 1
 3. Call the recursive function, to do a count and lastly append it to the river count sizes
"""

grid = [[1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1,0,1,  1, 0]]

def riverCountSizes(grid):
    # Get the number of rows and columns.
    rows, columns = len(grid), len(grid[0])
    # Directions tuple
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    # river_sizes = []
    river_sizes = []

    def riverCountSize(r, c):
        if r < 0  or c < 0 or r >= rows or c >= columns or  grid[r][c] == 0:
            return 0
        
        grid[r][c] = -1
        
        # call my recursive function to check the neightbours as well
        size = 1
        size += riverCountSize(r - 1, c)  # Check the cell above
        size += riverCountSize(r + 1, c)  # Check the cell below
        size += riverCountSize(r, c - 1)  # Check the cell to the left
        size += riverCountSize(r, c + 1)  # Check the cell to the right

        return size
      

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                count = riverCountSize(r, c)
                river_sizes.append(count)

    return river_sizes


#print(riverCountSizes(grid))

def river_sizes(grid):
    sizes = []
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
            return 0

        grid[row][col] = -1  # Mark the cell as visited

        size = 1
        size += dfs(row - 1, col)  # Check the cell above
        size += dfs(row + 1, col)  # Check the cell below
        size += dfs(row, col - 1)  # Check the cell to the left
        size += dfs(row, col + 1)  # Check the cell to the right

        return size

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                size = dfs(row, col)
                sizes.append(size)

    return sizes

print(river_sizes(grid))

