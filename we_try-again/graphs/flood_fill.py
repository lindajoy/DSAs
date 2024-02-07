"""
Took Notes on Graphs on:  7th Feb

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""
# 💡 SAMPLE INPUT.

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,2]]

# Really liked the flood fill question
# Here we approach it Recursively => The DFS Function always calls itself.
# 🤔 Take note of the originalColor and the color parameter

# Pictorial Representation: Or rather a Grid format representation
"""
    [1,1,1],
    [1,1,0],    💡 Given that the color is 2: We are looking at how we can transform the colors to be 2.
    [1,0,1]

    the output should be [[2,2,2],
                          [2,2,0],
                          [2,0,2]]

    Considering the input is , sr = 1, sc = 1, color = 1 

    [[1,1,1],
    [1,1,0],
    [1,0,1]]

    The output will remain the same since the original color is also 1, so  no transformation will take place:

    💡 This is the output

    [[1,1,1],
     [1,1,0],
    [1,0,1]]
"""
# Qustion for the interviewer:
   # 1. Can we always assume valid inputs?
  

# What is the time complexity? O(V+E) considering these are the number of rows and columns.

def floodFill(image, sr, sc, color):
    # Get the original color
    originalColor = image[sr][sc]

    # If the original color is equal to the color; then no transformation will take place
    if originalColor == color:
        return image
    
    # This is the recursive nature of the algorithm
    def dfs(row, col):
        # Check whether we are in range and whether the row and col is equal to the original color; then transformation can take place
        # What is happening ideally here is that we are looping through the entire matrix to transform the values
        if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == originalColor:
            image[row][col] = color
            # Goes in 4 directions: Top, Right, Bottom, Left
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
    # Calling our helper function
    dfs(sr, sc)

    return image

# A certain twist to the question, What if we wanted to verify whether each value in our matrix has been transformed?
# So we recieve the matrix and return a boolean saying whether we have a flood filled the matrix.

def floodFillboolean(matrix, sr, sc, color):
    startingColor = matrix[sr][sc]

    if color == startingColor:
        return matrix
    
    def dfs(r,c):
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == startingColor:
            matrix[r][c] =  color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    # Recursive call
    dfs(sr,sc)

    for r  in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != color:
                return False
    return True
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFillboolean(image, sr, sc, color))
