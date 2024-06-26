"""
You are given two arrays, A and B, each made up of n integers, they represent a grid with n columns and 2 rows, where A
is the upper row and b is the lower row, Your task is to go from the upper-left cell represented by (a [0]) 
to the bottom right of the cell
(represented by[n-1]), moving only right and down, so that the maximu value over which you pass is small as possible.
"""
def max_fish_value(A):
       n, m = len(A), len(A[0])
       dp = [[0] * m for _ in range(n)]
       dp[0][0] = A[0][0]

       for i in range(n):
           for j in range(m):
               if i > 0:
                   dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i][j])
               if j > 0:
                   dp[i][j] = max(dp[i][j], dp[i][j-1] + A[i][j])

       return dp[n-1][m-1]
 
   # Example usage:
A = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

B = [[10, 8, 9],
     [1, 12, 5],
     [3, 4, 15]]

A1 = [[1, -2],
     [3, 4]]


result = max_fish_value(A1)
result2 = max_fish_value(B)

print(f"Maximum fish value: {result}")


# The intution we are given a grid; And we need to return the maximum number of fish a fisherman can capture.
# The idea here is to initialize a grid with 0s, the idea is as we traverse through the entire grid, we are storing 
# The maximum number of fish we can capture on our previous cell.

# Here we are recieving the input as 2 different arrays:
#    We need to add them on one grid
#    Initialize dp[0][0] to have the value of the first element in the first position
def max_fish_value2(A, B):
     GRID = [A, B]
     ROWS, COLS = len(GRID), len(GRID[0])
     dp = [[0] * COLS for _ in range (ROWS)]
     # Actually this can also be:
     # C = A[0]
     dp[0][0] = GRID[0][0]

     # Traverse through the entire grid
     for row in range(ROWS):
          for col in range(COLS): 
               # Check if the row and column is within the range
               if row > 0:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col] + GRID[row][col])
               if col > 0:
                    dp[row][col] = max(dp[row][col], dp[row][col - 1] + GRID[row][col])



     return dp[ROWS- 1][COLS - 1]
arr1 = [1, -2]
arr2 = [3, 4]
print(max_fish_value2(arr1, arr2))


b = set()
b.add('a')
b.add('b')
print(list(b))
b.clear()
print(b)
