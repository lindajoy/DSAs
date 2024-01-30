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


