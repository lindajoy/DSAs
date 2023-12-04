'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

=> Each row must contain the digits 1-9 without repetition.
=> Each column must contain the digits 1-9 without repetition.
=> Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
  
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
'''
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

from collections import defaultdict

def isValidSudoku(board):
    colums = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    # The range of our columns and rows is 9 by 9
    for r in range((9)):
        for c in range((9)):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in colums[c] or
                board[r][c] in squares[(r // 3, c //3)]):
                return False
            
            colums[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c //3)].add(board[r][c])
    return True

print(isValidSudoku(board))

   

                
    