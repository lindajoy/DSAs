"""
💡 CHERRY PICKUP II

You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] 
represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:
    Robot #1 is located at the top-left corner (0, 0), and
    Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

    => From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    => When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    => When both robots stay in the same cell, only one takes the cherries.
    => Both robots cannot move outside of the grid at any moment.
    => Both robots should reach the bottom row in grid.

"""

# Initial perspective: I would use the DFS algorithm 
# Can we assume that we will always recieve valid inputs?


def cherryPickup(grid):
    visited = set()
    row, cols = len(grid), len(grid[0])
    robot1sum = 0

    def isValid(row, col):
        if row < 0 or col < 0 or col == len(grid[0]) or row == len(grid) or (row, col) not in visited:
            return False
        else:
            return True

    def dfs(row, col):
        if isValid(row, col):
            robot1 += dfs(row, col)
            res = max(dfs(row +1, col-1), dfs(row + 1, col), dfs(row, col +1))

        

    robot1 = dfs(0,0)
    robot2 = dfs(0, cols - 1)

