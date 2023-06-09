grid = [[1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1,0,1,  1, 0]]

def riverCountSizes(grid):
    # Get the number of rows and columns.
    rows, columns = len(grid), len(grid[0])
    # river_sizes = []
    river_sizes = []

    def riverCountSize(r, c):
        if r < 0  or c < 0 or r >= rows or c >= columns:
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


print(riverCountSizes(grid))