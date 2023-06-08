"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid2 = [[3,2],[1,0]]


def countNegatives(grid):
    rows, columns = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] < 0:
                count += 1
    return count

print(countNegatives(grid2))
print(countNegatives(grid))

