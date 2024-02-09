"""
Given an m x n matrix board containing 'X' and 'O', 
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = 
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
        ]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
"""
# The input here is a board.
# Output: Modified board with the captured areas.
# The above algorithm employs something called reverse thinking =>
# We are asked to capture the surrounded regions, but what if we captured the unsurrpunded regions first.

def capture_surrounded_areas(board):
    rows, columns = len(board), len(board[0])

    # Step 1: Capture the unsurrounded regions => Convert "O" to "T"
    def capture(r, c):
        # Check whether we are in bound of the graph dimensions
        if (r < 0 or c < 0 or r == rows or c == columns or board[r][c] != "O"):
            return 
        
        board[r][c] = "T"
        capture(r+1, c)
        capture(r-1, c)
        capture(r, c-1)
        capture(r, c+1)

    for r in range(rows):
        for c in range(columns):
            if (board[r][c] == "O" and (r in [0, rows -1]) and (c in [0, columns -1])):
                capture(r,c)

    # Step 2: Capture the other areas where "O" => "X"
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == "O":
                board[r][c] = "X"

    # Step 3. Uncapture the unsurrounded areas..🤣
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == "T":
                board[r][c] = "O"


"""
Takeaways: Employ reversible thinking; It helped me here hehe!
"""


# technical =>

