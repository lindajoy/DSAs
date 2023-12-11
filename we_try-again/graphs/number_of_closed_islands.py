"""
Given a 2D grid consists of 0s (land) and 1s (water).  
An island is a maximal 4-directionally connected group of 0s 
and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""

# One thing to note in this question is that the land cannot be a closed island if its at the edges.
# So a closed island should not be at the edges.

def closedIsland(grid):
    # Actually you could have started from here; Checking whether this grid really really exits.
    if not grid:
        return 0
    # Meaning that the grid at this point does not exist!
    # Initialize the number of rows and columns repectively.
    rows, columns = len(grid), len(grid[0])
    # Initialize an empty set
    visit = set()
    # Initialize number of closed islands
    closed_islands = 0

    def dfs(r, c):
        # Check whether the rows and columns are in bound.
        if (r < 0 or c < 0 or r == rows or c == columns):
            return 0 # False
        if grid[r][c] == 1 or (r, c) in visit:
            return 1 # return True
        
        # Makes a little bit of sense!
        visit.add((r, c))
        return min(dfs(r+1, c), dfs(r-1,c), dfs(r, c+1), dfs(r, c-1))
 
    for r in range(rows):
        for c in range(columns):
            # Forgot to add this statement.s
            if not grid[r][c] and (r,c) not in visit:   
             closed_islands += dfs(r, c)
    return closed_islands

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

print(closedIsland(grid))