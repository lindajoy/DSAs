"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
from collections import deque

def orangesRotting(oranges):
    rows, columns = len(oranges), len(oranges[0])
    fruits_queue = deque()
    time, fresh_fruits = 0, 0

    # Loop through the rows and columns
    for r in range(rows):
        for c in range(columns):
            if oranges[r][c] == 1:
                fresh_fruits += 1
            if oranges[r][c] == 2:
                fruits_queue.append([r,c])


    directions = [(1,0),(0,1),(-1,0), (0,-1)]
    while fruits_queue and fruits_queue > 0:
        for i in range(len(fruits_queue)):
            r, c = fruits_queue.popleft()

            for dr, dc in directions:
                row, col = dr + r, dc + c

                # If in bounds and fresh make rotten
                if (row < 0 or row == len(oranges) or col < 0 or col == len(oranges[0] or oranges[row][col] != 1)):
                    continue
                oranges[row][col] = 2
                fresh_fruits.append([row, col])
                fresh_fruits -= 1

        time += 1

    return time if fresh_fruits == 0 else -1

