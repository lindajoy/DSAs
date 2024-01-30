"""
The Maze
There is a ball in a maze with empty spaces and walls. 
The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The start and destination coordinates are represented by row and column indexes.
"""

# Whats the input? The input is a maze
# What is the output? A boolean: True if you can reach destination; False if you cannot reach the destination.

def maze(maze, startingPoint, endingPoint):
    # Validate the input
    if not maze:
        return False
    
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = [startingPoint[0], startingPoint[1]]

    def dfs(x, y):
        if (x, y) == endingPoint:
            return True
        if (x < 0 or y < 0 or y== len(maze[0]) or x == len(maze) or maze[x][y] == 1 or  (x, y) in visited):
            return False
        for dx, dy in directions:
            new_x, new_y = x + dx, dy + y
            visited.add((new_x, new_y))
            path.append((new_x, new_y))
            res = dfs(new_x, new_y)
            if res:
                return True
            path.pop()
        return False

    if dfs(startingPoint[0], startingPoint[1]):
        return True
    else:
        return False
