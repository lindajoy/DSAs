"""
Consider an m* n grid containing cells with three potential values:

    0, which indicates an unoccupied cell
    1, representing a freshly picked orange.
    2, indicating a rotten orange.

Any fresh orange that is 4–directionally adjacent to a rotten orange will also turn rotten with each passing minute.
Your task is to determine the minimum time required for all cells to have rotten oranges. 
In case, this objective cannot be achieved, return -1

"""

# What does this question ask us about?
# Whats the input is the best question? Heheehe
# A matrix
# Returns how many minutes it takes for all the rotten oranges in the matrix to rot
# If the oranges are not all rotten , then we need to return -1

# One of the hints that is supposed to indicate that we should use BFS is the keyword minimum.
# One thing about BFS is that it will always return the shortest path/time/or whatever,  whenever it comes to graph problems, 
# This is the first algorithm you should think about.

# TIME COMPLEXITY IS O(N*M)
# SPACE COMPLEXITY IS O(N*M)

from collections import deque

def rotten_oranges(grid):
    # Initialize the number of rows and columns
    rows, columns = len(grid), len(grid[0])

    # Initialize a visit set.
    visited = set()
    # Initialize the number of minutes
    minutes = 0
    # Initialize the number of fresh_count
    fresh_count = 0

    q = deque()
    # At this point, we are filling our queue with the indexes of the rotten oranges.
    # And marking them as visited, while also keeping count of the fresh oranges, because if there are no fresh oranges, then there is no need
    # To loop through the entire grid.🙃
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 2:
                q.append((r,c))
                visited.add((r,c))
            elif grid[r][c] == 1:
                fresh_count += 1


    # Returns 0, if there no fresh oranges.
    if fresh_count == 0:
        return 0
    

    # Breadth First Search
    while q:
        size = len(q)
        for _ in range(size):
            # Whenever you use a queue always ensure that you are popping the last element.
            row, col = q.popleft()
            # Directions that allow you to go in all 4 directions.
            directions = [[0,1], [1,0],[0,-1],[-1,0]]
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                    grid[r][c] = 2
                    fresh_count -=1
        minutes += 1

    # This is something I have been struggling with why do we need to substract one from minutes? 🤔
    return minutes - 1 if fresh_count == 0 else -1

print(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))

