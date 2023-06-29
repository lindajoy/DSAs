"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room.

We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. 
If it is impossible to reach a Gate, that room should remain filled with INF

Input:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

Output:

3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
"""
"""
BFS Implementation => Does not work since my input is wrong.
"""
matrix = [['INF', -1, 0, 'INF'], 
          ['INF', 'INF', 'INF', -1],
          ['INF', -1, 'INF', -1],
          [0, -1, 'INF', 'INF']]

from collections import deque

def wallandgates(matrix):
    # Wall and gates
    rows, columns = len(matrix), len(matrix[0])

    visited = set()

    q = deque()

   
    def addRoom(row, column):
        # Check whether its in bound
        if (row < 0 or row == rows or column < 0 or column == columns or (r,c) in visited or matrix[r][c] == -1):
            return       
        visited.add((row , column))
        q.append([row , column])

    # Loop through the rows and the columns
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
              q.append([r,c])
              visited.add((r,c))

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            matrix[r][c] = dist
            addRoom(r+1, c)
            addRoom(r-1, c)
            addRoom(r, c+1)
            addRoom(r, c-1)
        dist += 1
    return matrix

print(wallandgates(matrix))


def wallandgatesDepthSearch(matrix):
    
    if not matrix:
        return []
        
    rows, columns = len(matrix), len(matrix[0])
    visited = set()

    directions = [(-1,0), (0,1), (0,-1), (1,0)]

    def dfs(x, y, dis):
        for dx, dy in directions:
            nx,ny = x +dx, y + dy

            if 0<=nx<rows and 0<= ny<columns and matrix[nx][ny] > matrix[x][y]:
                matrix[nx][ny] = dis + 1
                dfs(nx,ny, dis + 1)

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                dfs(r, c, 0)

print("😱",wallandgatesDepthSearch(matrix))



    