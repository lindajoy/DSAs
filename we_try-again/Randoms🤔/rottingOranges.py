"""
You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

INPUT: grid = [[2,1,1],[1,1,0],[0,1,1]]
OUTPUT: 4

INPUT: grid = [[2,1,1],[0,1,1],[1,0,1]]
OUTPUT: -1
"""

# 💡: This solution would not work I guess because of the ordering.
def minimumNumberOfMinutes(grid):
    minutes = 0
    rows, columns = len(grid), len(grid[0])
    fresh_fruits = 0
    visited_set = set()

    def dfs(row, column):
        minutes = 0
        if row < 0 or row >= rows or column < 0 or column >= columns or (row,column) in visited_set:
            return 0
        
        visited_set.add((row, column))
        grid[row][column] = 2
        minutes += 1
        fresh_fruits -= 1

        dfs(row + 1, column)#Go down
        dfs(row-1, column)#Go up
        dfs(row, column + 1)#Go right
        dfs(row, column - 1)#Go left

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                fresh_fruits += 1

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 2:
                dfs(r,c)
    return minutes if fresh_fruits == 0 else -1

# Solution 2: Lemme see
def orangesRotting(grid):
    if not grid:
        return -1
    
    m, n = len(grid), len(grid[0])
    fresh_count = 0
    rotten = []
    
    # Count fresh oranges and store positions of rotten oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                rotten.append((i, j, 0))  # (x, y, minutes)
    
    # Define the four directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0
    
    while rotten:
        # Here we are destructuring...
        x, y, minutes = rotten.pop(0)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # Mark fresh orange as rotten
                fresh_count -= 1
                rotten.append((nx, ny, minutes + 1))
    
    return minutes if fresh_count == 0 else -1
