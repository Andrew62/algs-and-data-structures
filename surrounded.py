def is_surrounded(board, row_idx, col_idx):
    cols = len(board[0])
    col_left = col_idx - 1
    col_right = col_idx + 1
    
    rows = len(board)
    row_up = row_idx - 1
    row_down = row_idx + 1
    while col_left >= 0 and col_right <= cols and row_up >= 0 and row_down <= rows:
        if (board[row_idx][col_left] == "X" and board[row_idx][col_right] == "X" and
            board[row_up][col_idx] == "X" and board[row_down][col_idx] == "X"):
            print("Is surrounded", row_idx, col_idx)
            return True
        if board[row_idx][col_left] != "X":
            col_left -= 1
        if board[row_idx][col_right] != "X":
            col_right += 1
        if board[row_up][col_idx] != "X":
            row_up -= 1 
        if board[row_down][col_idx] != "X":
            row_down += 1
    return False
        

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    x = "X"
    o = "O"
    rows = len(board)
    cols = len(board[0])
    # not going to check the boards b/c explanation
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if board[row][col] == o and is_surrounded(board, row, col):
                board[row][col] = x
    # return board
                    
                        

if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    solve(board)
    print(board)