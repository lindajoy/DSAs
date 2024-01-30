"""
Consider an m* n grid containing cells with three potential values:

    0, which indicates an unoccupied cell
    1, representing a freshly picked orange.
    2, indicating a rotten orange.

Any fresh orange that is 4–directionally adjacent to a rotten orange will also turn rotten with each passing minute.
Your task is to determine the minimum time required for all cells to have rotten oranges. 
In case, this objective cannot be achieved, return -1

"""
from collections import deque
def rotten_oranges(grid):
    # Initialize the number of rows and columns
    rows, columns = len(grid), len(grid[0])
    visited = set()
    # Initialize the number of minutes
    minutes = 0
    # Initialize the number of fresh_count
    fresh_count = 0

    q = deque()
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 2:
                q.append((r,c))
                visited.add((r,c))
            elif grid[r][c] == 1:
                fresh_count += 1


    if fresh_count == 0:
        return 0
    

    # Breadth First Search
    while q:
        size = len(q)

        for _ in range(size):
            row, col = q.popleft()
            directions = [[0,1], [1,0],[0,-1],[-1,0]]
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                    grid[r][c] = 2
                    fresh_count -=1
        minutes += 1


    return minutes - 1 if fresh_count == 0 else -1

print(rotten_oranges([[2,1,1],[1,1,0],[0,1,1]]))

# Can we try doing it using DFS

def rotten_oranges_dfs(grid):
    # Lets validate the input
    if not grid:
        return 0
    
    rows, columns = len(grid), len(grid[0])
    visited = set()
    minutes, fresh_fruits = 0, 0

    def dfs(r, c):
        if (r < 0 or c < 0 or r == rows or c == columns or (r,c) in visited):
            return
        

    for r in range(rows):
        for c  in range(columns):
            if grid[r][c] == 1:
                fresh_fruits += 1
                dfs(r,c)

