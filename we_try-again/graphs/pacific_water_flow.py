"""
Imagine an island with a rectangular shape that touches both the Pacific and Atlantic oceans. 
The northern and western sides meet the Pacific, while the southern and eastern sides touch the Atlantic. 
This island is divided into square cells.
To depict the height above sea level of each cell, we use an integer matrix, heights, of size (m×n). 
Here, heights[r][c] represents the elevation of the cell at coordinate 
(r,c), When heavy rain pours down on the island every few months, water flows from the island to both the Pacific and Atlantic oceans. 
The path of flow depends on the heights of the cells.
"""

def PacificAtlanticWaterFlow(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    # Create A DFS function which is a recursive function.
    def dfs(r,c, visit, prevHeights):
        # Check whether we are within range
        if ((r, c) in visit or r < 0 or r == ROWS or c < 0 or c == COLS or  heights[r][c] < prevHeights):
            return
        # Add the two co-ordinates the set
        visit.add((r,c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    # Loop through the rows
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS-1, atl,heights[r][COLS-1])

    # Loop through the columns
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    # Find res
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])

    return res

heights = [[1, 1, 0, 1], [0, 1, 0, 2], [0, 0, 1, 1]]
heights4 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(PacificAtlanticWaterFlow(heights4))
print(PacificAtlanticWaterFlow(heights))



