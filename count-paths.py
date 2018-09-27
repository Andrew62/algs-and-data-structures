"""
Count the number of paths through a grid assuming you want to start in 
the top left and finish in the bottom right. Valid cells are marked 
with 1. Other values are not navigable

Example:
[
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

output: 2
"""

class DFS(object):
    def __init__(self, board):
        self.board = board
        self.visited = []
        self.rows = len(board)
        self.cols = len(board[0])

        # target cell will always be bottom right for this example
        self.target_c = self.cols - 1
        self.target_r = self.rows - 1

    def count_paths(self, current_row=0, current_col=0):
        if current_row == self.target_r and self.target_c == current_col:
            return 1
        proposed_move = (current_row, current_col + 1)
        paths = 0
        if current_col + 1 < self.cols and proposed_move not in self.visited and self.board[proposed_move[0]][proposed_move[1]] == 1:
            if proposed_move != (self.target_r, self.target_c):
                self.visited.append(proposed_move)
            paths += self.count_paths(*proposed_move)
        proposed_move = (current_row + 1, current_col)
        if current_row + 1 < self.rows and proposed_move not in self.visited and self.board[current_row + 1][current_col] == 1:
            if proposed_move != (self.target_r, self.target_c):
                self.visited.append(proposed_move)
            paths += self.count_paths(*proposed_move)
        return paths


def count_paths(board):
    dfs = DFS(board)
    return dfs.count_paths(0, 0)


if __name__ == "__main__":
    board = [
        [1, 1, 0],
        [1, 1, 1],
        [1, 1, 1]
    ]    
    print(count_paths(board))