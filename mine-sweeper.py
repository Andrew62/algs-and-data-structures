"""
You are given a 2D char matrix representing the game board. 'M' represents an unrevealed 
mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square 
that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit 
('1' to '8') represents how many mines are adjacent to this revealed square, and finally 
'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares 
('M' or 'E'), return the board after revealing this position according to the following rules:

    If a mine ('M') is revealed, then the game is over - change it to 'X'.
    If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Note:

    The range of the input matrix's height and width is [1,50].
    The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
    The input board won't be a stage when game is over (some mines have been revealed).
    For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

"""

checked = []

def updateBlank(board, row, col):
    n_rows = len(board)
    n_cols = len(board[0])
    mine_count = 0
    checked.append((row, col))
    for ridx in range(max(0, row - 1), min(row + 2, n_rows)):
        for cidx in range(max(0, col - 1), min(col + 2, n_cols)):
            if board[ridx][cidx] == "M":
                mine_count += 1
    if mine_count == 0:
        board[row][col] = "B"
        for ridx in range(max(0, row - 1), min(row + 2, n_rows)):
            for cidx in range(max(0, col - 1), min(col + 2, n_cols)):
                if (ridx, cidx) not in checked:
                    checked.append((ridx, cidx))
                    board = updateBlank(board, ridx, cidx)
    else:
        board[row][col] = str(mine_count)
    
    return board


def updateBoard(board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        if board[row][col] == "E":
            # update all cells until we get near a mine
            board = updateBlank(board, row, col)
        # no change
        return board


if __name__ == "__main__":
    board = [
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ]

    click = [1, 2]

    expected_output = [
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'X', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ]

    board = [
        ["E","E","E","E","E"],
        ["E","E","M","E","E"],
        ["E","E","E","E","E"],
        ["E","E","E","E","E"]
    ]
    click = [3, 0]
    expected_output = [
        ["B","1","E","1","B"],
        ["B","1","M","1","B"],
        ["B","1","1","1","B"],
        ["B","B","B","B","B"]
    ]

    updated_board = updateBoard(board, click)
    for ridx, row in enumerate(updated_board):
        for cidx, col in enumerate(row):
            if col != expected_output[ridx][cidx]:
                print(f"Boards don't match at {ridx} {cidx}")
    for row in updated_board:
        print(row)
        