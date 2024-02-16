"""
You are given two arrays, A and B, each made up of n integers, they represent a grid with n columns and 2 rows, where A
is the upper row and b is the lower row, Your task is to go from the upper-left cell represented by (a [0]) to the bottom right of the cell
(represented by[n-1]), moving only right and down, so that the maximu value over which you pass is small as possible.
"""
# def dfs(grid, i=0, j=0, max_val=float('inf')):
#     if i == len(grid) - 1 and j == len(grid[0]) - 1:
#         return min(max_val, grid[i][j])

#     directions = [(1, 0), (0, 1)]  # Right and Down
#     min_max = float('inf')

#     for dx, dy in directions:
#         x, y = i + dx, j + dy
#         if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
#             min_max = min(min_max, dfs(grid, x, y, max(max_val, grid[i][j])))
    
#     return min_max

# grid = [[1, 2, 3], [4, 5, 6]]
# result = dfs(grid)
# print("Minimum maximum value passing through:", result)

def maxFish(grid):
  nc=grid[0]
  for i in range(len(nc)):
    if(i!=0):
      nc[i]+=grid[0][i-1]
  
  for i in range(1,len(grid)):
    for j in range(len(grid[0])):
      if (j!=0):
        nc[j]=max(grid[i][j]+nc[j], nc[j-1]+grid[i][j])
      else:
        nc[j]+=grid[i][j]
  return nc[len(grid[0])-1]
  
grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(maxFish(grid))
# print(maxFish([1, 2],[3, 4],[5, 6]))
print(maxFish([[7, 2, 9],[1, 5, 3],[4, 8, 6]]))
