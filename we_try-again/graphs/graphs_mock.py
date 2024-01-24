"""
We can picture the country as a matrix there:
    - '1' -> is a road
    - '0' -> is a farm or just a place we cannot build
    - '-1' -> is cities we want to connect

Find a path that connects all the cities (-1) together.

HMM, this question is deeper than it looks. 🤔

Question Here To the interviewer here can be:
    1. Can we assume that there will always be a path that connects all the cities together (-1)?
       i) How do we account for the case where a path cannot be formed what should we return?
    2. When returning the positions, should we we also include the positions of -1s(cities or we can just skip them)?
    3. When you say the output is positions => Should be a list of positions?  
    4. When we say the output should be a list of positions are we considering the longest path or shortest path? Because.. `THIS IS THE PART WHERE YOU SHOW WHAT YOU HAVE OBSERVED ON THE DIAGRAM`
"""

# Time Complexity would be 0( len(grid) + len(grid[0]) )
matrix = [
    [1, 1, 1, 1, 1, -1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, -1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, -1]
]

outputMatrix = [
    [1, 1, 1, 1, 1, -1_],
    [1, 0, 0, 0, 0, 1_],
    [1, 0, -1_, 0, 0, 1_],
    [1, 0, 1_, 1_, 1_, 1_],
    [1, 0, 1, 0, 0, 1_],
    [1, 1, 1, 1, 1, -1_]
]

# Here I am thinking about the two graph algorithms: BFS and DFS.
# Assumptions made:
#   1. The output is a list of positions.

# Lets create a Pseudocode for this right?
# So how would solving it using DFS look like?
"""
PSEUDOCODE:

1. Loop through the entire matrix, 
"""

def find_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == -1:


   



