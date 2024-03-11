"""
Was asked this question during the recent MS Interview:

You are given a chess board (2D array) where each square is assigned a non negative integer. 
Two rooks are to be placed on the chess board such that they don't 
kill each other and sum of the values of the squares they are placed in should be maximim.
Return the maximum sum.

Input:
0 1 5
3 0 5
1 4 1

Output: 9
"""
"""
Another Example:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
 
Output: Maximum sum: 0

Another Example:
[[2, 2, 2],
 [2, 2, 2],
 [2, 2, 2]]

Output: Maximum sum: 4
"""

GRID = [[2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]]

GRID2 = [[0, 1, 5],
        [3, 0, 5],
        [1 , 4 ,1]]

def solution(A):
    max_val = 0
    a = {}
    b = []

    for i in range(len(A)):
        for j in range(len(A[i])):
            a[str(i) + str(j)] = A[i][j]
            b.append([i, j])

    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            sum_val = a[str(b[i][0]) + str(b[i][1])] + a[str(b[j][0]) + str(b[j][1])]
            if b[i][0] != b[j][0] and b[i][1] != b[j][1] and max_val < sum_val:
                max_val = sum_val

    return max_val

print(solution(GRID))
print(solution(GRID2))
