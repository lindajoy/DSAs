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

def minimumNumberOfMinutes(grid):
    minutes = 0
    rows, columns = len(grid), len(grid[0])
    fresh_fruits = 0
    visited_set = set()

    def dfs(row, column):
        minutes = 0
        print(fresh_fruits)
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

print(minimumNumberOfMinutes([[2,1,1],[1,1,0],[0,1,1]]))
