"""
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

def floodFill(image, sr, sc, color):
    originalColor = image[sr][sc]

    if originalColor == color:
        return image
    
    # This is the recursive nature of the algorithm
    def dfs(row, col):
        # Check whether we are in range.
        if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == originalColor:
            image[row][col] = color
            # Goes in 4 directions: Top, Right, Bottom, Left
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

    dfs(sr, sc)

    return image

