"""
NUMBER OF ENCLAVES.

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
"""

# A question to ask the interviewer before solving this problem:
# i) Is it okay to mutate the input?

def numberOfEnclaves(grid):
    rows, columns = len(grid), len(grid[0])
    land_inside_grid, bordered_land = 0, 0
    visit = set()

    def dfs(r, c):
        # check whether in bound
        if (r < 0 or c < 0 or  c == columns or r == rows or not grid[r][c] or(r,c) in visit):
            return 0
        visit.add((r,c))
        res = 1
        directions = [[1,0], [0,1], [0,-1], [-1 ,0]]

        for  dr, dc in directions:
            res += dfs(dr+ r, dc + c)
        return res
        
    # Initialize the number of lands and border-land
    for r in range(rows):
        for c in range(columns):
            land_inside_grid += grid[r][c]
            if (grid[r][c] == 1 and (r,c) not in visit and (c in [0, columns -1] or r in [0, rows-1])):
                bordered_land += dfs(r, c)

    return land_inside_grid - bordered_land

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
grid2 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

print(numberOfEnclaves(grid2))
