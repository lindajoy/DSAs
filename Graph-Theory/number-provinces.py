"""
Let’s say we have n number of cities, and some of them are connected, while some are not. 
If a city A is connected directly with city B, and city B is connected directly with city C, 
then we can say that city A is connected indirectly with city C.

A province is a group of directly or indirectly connected cities with no other cities outside of the group.

An (n × n) matrix, is_city_connected, is given, where is_city_connected[i][j] = 1 indicates that the ith and the jth
cities are directly connected. Otherwise, the value is is_city_connected[i][j] = 0.

Use this information to return the total number of provinces.

"""
grid1 = [[1,1,0],[1,1,0],[0,0,1]]
grid2 = [[1,0,0],[0,1,0],[0,0,1]]
grid3 = [[1,1,0,1],[1,1,0,1],[0,0,1,0],[1,1,0,1]]

"""
This question can be solved by either:
   1. BFS Pattern
   2. DFS Pattern
   3. Union Find Algorithm

💡 Discovered something interesting while working on this problem n*n means the number of columns and rows are equal.

The input in this case is Matrix.
The Output in this case is the Number of Total Provinces.

The value 1 indicates at the very least that the cities are connected.
The value 0 indicates that the city is not connected.
"""

# 💡 IMPLEMENTATION 1: DEPTH FIRST SEARCH

def is_city_connetected(matrix):

    # Since the its an n by n matrix there's no need of getting the number of rows and columns.
    matrix_dimensions = len(matrix)

    # We need to have this matrix so that when we visit a particular dimension we mark it as True.
    visited = [False] * matrix_dimensions

    # Number of provinces 
    provinces = 0

    def dfs(city):
        # Mark it as visited
        visited[city] = True

        for neighbour in range(matrix_dimensions):
            if matrix_dimensions[city][neighbour] == 1 and not visited[neighbour] == True:
                dfs(neighbour)

    
    for city in range(matrix_dimensions):
        if not visited[city]:
            dfs(city)
            provinces += 1

    return provinces

# 💡 IMPLEMENTATION 2: BREADTH FIRST SEARCH

from collections import deque

def is_city_connected_breadth(city):
    # Since the its an n by n matrix there's no need of getting the number of rows and columns.
    matrix_dimensions = len(city)

    # We need to have this matrix so that when we visit a particular dimension we mark it as True.
    visited = [False] * matrix_dimensions

    # Number of provinces 
    provinces = 0

    def bfs(city):
        queue = deque()
        queue.append(city)

        while queue:
            current_city = queue.popleft()
            visited[current_city] = True

        for c in range(matrix_dimensions):
            if matrix_dimensions[current_city][c] == 1 and not visited[c] == True:
                bfs(c)


    for r in range(matrix_dimensions):
        if not visited[city]:
            bfs(city)
            provinces += 1

    return provinces
    