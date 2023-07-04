"""
Depth First Traversal => Is a graph traversal Algorithm (Algorithms to visit every vertex of the graph)
It may contain cycles(A node may be visited twice so we have to always keep track of the visited nodes by either using a set or an array)
I prefer using a set since a set holds no duplicates.

The basic Pseudocode is:
1. Loop through rows and columns
2. Mark as visited 
3. Check the neigbors as well whether they are 1 or not.

Applications of Depth Search.
1. Detecting a cycle in a graph.
2. Topological Sorting.
3. Finding strongly connected components.
4. Path Finding.

Number Of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Link: https://leetcode.com/problems/number-of-islands/description/


💡 This is a recursive function that calls the dfs function and finds the islands from the matrix.
"""

def numIslands(self, grid):
    if not grid:
        return 0
    
    count = 0

    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "1":
                self.dfs(grid,row, column)
                count += 1
    return count


def dfs(self, grid, row, column):

    if row < 0 or column < 0 or row>=len(grid) or column>=len(grid[0]):
        return
    
    # Mark current one as visited
    grid[row][column] = "#"
    
    self.dfs(grid, row + 1, column)
    self.dfs(grid, row, column + 1)
    self.dfs(grid, row - 1, column)
    self.dfs(grid, row, column -1)



