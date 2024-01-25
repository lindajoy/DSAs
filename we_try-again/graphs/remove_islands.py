# 💡 Remove Islands
"""
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. 
The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. 

An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent) 
and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s 
isn't an island if any of those 1s are in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist. 
In other words, it doesn't have to be a straight vertical line or a straight horizontal line; 
it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.

Write a function that returns a modified version of the input matrix, where all of the islands are removed. You remove an island by replacing it with 0s.

Naturally, you're allowed to mutate the input matrix.

matrix = 
[
  [0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 0],
  [0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 1, 0],
  [0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0],
]

Sample Output: [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
] 
// The islands that were removed can be clearly seen here:
// [
//   [ ,  ,  ,  ,  , ],
//   [ , 1,  ,  ,  , ],
//   [ ,  , 1,  ,  , ],
//   [ ,  ,  ,  ,  , ],
//   [ ,  , 1, 1,  , ],
//   [ ,  ,  ,  ,  , ], 
// ]
"""

"""
This what I have in mind: Idea came from Number Of Enclaves Question.
1. First we mark the borders' neighbours as visited

"""
# We are making progress 💡
# My solution works: Well on my input
def removeIslands(matrix):
    # Validate the input
    if not matrix:
        return matrix
    
    rows, columns = len(matrix), len(matrix[0])
    visit = set()

    def markedAsVisited(r,c):
        if (r < 0 or c < 0 or c == columns or r == rows or matrix[r][c] == 0 or  (r,c ) in visit):
            return
        visit.add((r,c))
        directions = [[1,0], [0,1], [0,-1], [-1 ,0]]
        for dr,dc in directions:
            markedAsVisited(dr+r , dc + c)


    def dfs(r,c):
        if (r < 0 or c < 0 or c == columns or r == rows or matrix[r][c] == 0 or (r,c ) in visit):
            return
        matrix[r][c] = 0
        visit.add((r,c))
        directions = [[1,0], [0,1], [0,-1], [-1 ,0]]
        for dr,dc in directions:
            dfs(dr+r , dc + c)

    for r in range(rows):
        for c in range(columns):
            # Get land and neighbours for the border elements
            if (matrix[r][c] == 1 and (r,c) not in visit and (c in [0, columns-1] or r in [0, rows-1])):
                markedAsVisited(r,c)
            
    for r in range(rows):
        for c in range(columns):
                dfs(r,c)
                
    return matrix

input = [
  [0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 0],
  [0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 1, 0],
  [0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0],
]

input2 = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1],
]

print(removeIslands(input2))


