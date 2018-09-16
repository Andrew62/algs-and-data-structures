"""
https://www.hackerrank.com/challenges/botclean?hr_b=1
"""

from typing import List, Tuple
from itertools import product

Board = List[List[str]]

# board tokens 
bot_token = 'b'
dirt_token = 'd'

# moves
up = "UP"
left = "LEFT"
right = "RIGHT"
down = "DOWN"
clean = "CLEAN"

def find_dirt(posr: int, posc: int, board: Board) -> List[Tuple[int, int]]:
    rows = len(board)
    cols = len(board[0])

    # initialize bfs variables
    q = [(posr, posc)]
    visited = [(posr, posc)]
    dirty_cells = []

    _moves = [-1 , 0, 1]
    while len(q) > 0:
        current_r, current_c = q.pop(0)
        # check all around a given coordinate
        for delta_r, delta_c in product(_moves, _moves):
            move_r = current_r + delta_r
            move_c = current_c + delta_c
            move_to_check = move_r, move_c
            if move_to_check not in visited and 0 <= move_r < rows and 0 <= move_c < cols:
                maybe_r, maybe_c = move_to_check
                if board[maybe_r][maybe_c] == dirt_token:
                    dirty_cells.append(move_to_check)
                visited.append(move_to_check)
                q.append(move_to_check)
    return dirty_cells


def manhattan_dist(x_1, y1, x_2, y_2) -> float:
    return abs(x_2 - x_1) + abs(y_2 - y1)

def find_closest_dirt(posr: int, posc: int, board: Board) -> Tuple[int, int]:
    dirt_locations = find_dirt(posr, posc, board)
    if len(dirt_locations) > 1:
        closest = float('inf')
        out_pos = -1, -1
        for dirt in dirt_locations:
            dist = manhattan_dist(posc, posr, dirt[1], dirt[0])
            if dist < closest:
                closest = dist
                out_pos = dirt
        return out_pos
    return dirt_locations[0]

def decide_move(posr: int, posc: int, board: Board) -> str:
    if board[posr][posc] == dirt_token:
        return clean
    dirt_r, dirt_c = find_closest_dirt(posr, posc, board)
    if dirt_r < 0 or dirt_c < 0:
        raise RuntimeError("No dirt to clean")

    delta_r = dirt_r - posr
    delta_c = dirt_c - posc
    if 0 < delta_r :
        return down
    elif 0 > delta_r:
        return up
    elif 0 < delta_c:
        return right
    elif 0 > delta_c:
        return left

        
def next_move(posr: int, posc: int, board: Board):
    print(decide_move(posr, posc, board))


if __name__ == "__main__":
    board = [
        ['d', '-', 'm', '-', '-'], 
        ['-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-']
    ]
    next_move(0, 2, board)