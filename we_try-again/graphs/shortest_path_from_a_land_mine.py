"""
Given a maze in the form of a rectangular matrix, filled with either O, X, or M, where O represents an open cell, 
X represents a blocked cell, and M represents landmines in the maze, 
find the shortest distance of every open cell in the maze from its nearest mine.
We are only allowed to travel either of the four directions, and diagonal moves are not allowed. 
We can assume cells with the mine have distance 0. Also, blocked and unreachable cells have distance -1.
"""

# Questions for the interviewer: 🤔

# By distance, you mean the length of the shortest paths to visit all the mines? 
# (To answer the question above we are notified from the problem description that cells with the mine have the distance 0)
# Is it possible to have a grid that does not have land mines?

# Hints we can pick up:
# 1. In the question above, we are asked to find the shortest distance, (shortest) encourages us to use Breadth First search algorithm?

from collections import deque

def shortest_distance_to_mine(maze):
    if not maze:
        return []
    
    rows, cols = len(maze), len(maze[0])
    distances = [[-1] * cols for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    mines = deque()
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == "M":
                distances[i][j] = 0
                mines.append((i,j))
    
    while mines:
        x , y  = mines.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (x in range(rows) and y in range(cols) and maze[nx][ny]== 0 and distances[nx][ny] == -1 ):
                distances[nx][ny] = distances[x][y] + 1
                mines.append((nx, ny))

    return distances

