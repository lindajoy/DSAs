"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
def maxAreaOfIsland( grid) -> int:
    rows, columns = len(grid), len(grid[0])
    visited = set()
    area = 0

    def dfs(r, c):
        # Check whether its within range.
        if (r < 0 or r == rows or c < 0 or c== columns or grid[r][c] == 0 or (r,c) in visited):
            return 0

        visited.add((r,c))
        return 1 + dfs(r+1, c) +  dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

    for r in range(rows):
        for c in range(columns):
            area = max(area, dfs(r,c))

    return area
        