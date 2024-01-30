"""
💡 SEARCH IN MAZE
Given a 2D array of black and white entries representing amaze with designated entrance and exit points, find a path from the entrance to the exit, if one exists.
"""
# You are given the starting and ending points 
# This solution is from Elements of Programming

from collections import namedtuple

WHITE, BLACK = range(2)
Coordinate = namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, startingPoint, endingPoint):
    path = []
    # Performs DFS to find a feasible path
    def search_maze_helper(cur):
        # Checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])  and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == endingPoint:
            return True
        if any(map(search_maze_helper(Coordinate (
cur.x - 1, cur.y), Coordinate(cur.x + 1, cur.y), Coordinate( cur.x, cur,y - 1), Coordinate(cur.x, cur.y + 1)))):
            return True
        
        # Cannot find path, remove the entry added in the path.append(cur)
        del path[-1]
        return False
    

    if not search_maze_helper(startingPoint):
        return []
    return path


# Another solution if that makes more sense.
# The good thing about this question is that we are only searching for a path
# It does not matter whether the path is short or long.
# If it was specied that we should find the shortest path, we could have used BFS.

def searchPathInMaze(maze, start, end):
    # Define directions: up, down,left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    path = [(start[0], start[1])]

    def is_valid(x, y):
        # Check if the coordinates are within the maze boundaries and it's not a wall
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1
    

    def dfs(x, y, visited, path):
        if (x, y) == end:
            return True
        visited.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x +dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                path.append((new_x, new_y))
                if dfs(new_x, new_y, visited, path):
                    return True
                # Removes the last appended element
                path.pop()
        return False
    
    if dfs(start[0], start[1], visited, path):
        return path
    else:
        return None

# Using Breadth First Search(BFS)
# 🥹 The good thing about BFS is that you are always getting the shortest path ⨒
from collections import deque

def hasPathBFS(maze, start, destination):
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append(start)
    visited.add(tuple(start))

    while queue:
        current = queue.popleft()
        if current == destination:
            return True
        
        for dx, dy in directions:
            x, y = current[0], current[1]
            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                
            if (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))
        
        return False





