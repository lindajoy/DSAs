"""
COUNT SUB ISLANDS

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).

An island is a group of 1's connected 4-directionally (horizontal or vertical). 
Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

INPUT:
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output = 3
"""

# 0s (Water) and 1s (Land).
# We need to find all the islands in Grid 1, save their indices in one matrix.
# After saving the points in a grid and loop through the same for the second grid.


def count_sub_islands(grid1, grid2):
    ROWS_1, COLUMNS_1 = len(grid1), len(grid1[0])
    ROWS_2, COLUMNS_2 = len(grid2), len(grid2[0])
    visit1, visit2 = set(), set()

    for r1 in range(ROWS_1):
        for c1 in range(COLUMNS_1):
            dfs(r1, c1)


    for r2 in range(ROWS_2):
        for c2 in range(COLUMNS_2):
            dfs(r2, c2)