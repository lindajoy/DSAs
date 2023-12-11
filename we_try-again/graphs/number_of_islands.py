"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
"""

#   💡 One thing to note while reading the question is the directions:  
#   The question states that we should move horizontally and vertically; not diagonally 🤔
#   Another thing I have learnt is when working with any Data structure question something that should become second nature
#   is to always start by validating the input.
#   In this solution we use Breadth First search, however the depth first search can also be applied!!

from collections import deque

grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numberOfIslands(grid):
    # Validate the input value given.
    if not grid:
        return 0
    
    rows, cols  = len(grid), len(grid[0])
    # Initialize a visit set, to add co-ordinates that have already been visited.
    # Why set you ask? Because sets contain unique values.
    visit = set()
    # Initialize number of islands
    number_of_islands = 0

    # The bfs function will be running untill the queue is empty
    def bfs(r, c):
        q = deque()
        # Add them as a tuple
        visit.add((r,c))
        q.append((r,c))
        while q:
           
            # Did you know when using queues the pop does not take any argument...
            # So this would not work: 
            #       You can also do row, col = q.pop(0)
            # However if you wanted to implement this using dfs you would replace:
            #  row, col = q.popleft() with row, col = q.pop()
            # 💡😄 Brings out the same answer!! 🎉
            
            row, col = q.popleft()
            directions = [[1,0],[0,1] ,[-1,0],[0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if(r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r, c)
                number_of_islands += 1
    return number_of_islands
                 

print(numberOfIslands(grid))
print(numberOfIslands(grid2))