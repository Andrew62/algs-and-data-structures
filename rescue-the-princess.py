"""
https://www.hackerrank.com/challenges/saveprincess?hr_b=1

input:

3
---
-m-
p--

output:

DOWN
LEFT

Input is provided on separate lines. Starting position is always center

Steps:
find 'm' token coordinates
find 'p' token coordinates
find shortest path and output in text {UP, DOWN, LEFT, RIGHT}
"""


class FindThePrincess(object):
    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"
    bot_token = 'm'
    princess_token = 'p'

    def __init__(self, grid_size, grid):
        self.grid_size = grid_size
        self.grid = grid
        self.bot_pos = None
        self.princess_pos = None
        self.find_initial_positions()

    def find_initial_positions(self):
        for ridx, row in enumerate(self.grid):
            for cidx, col in enumerate(row):
                if col == self.princess_token:
                    self.princess_pos = ridx, cidx
                elif col == self.bot_token:
                    self.bot_pos = ridx, cidx
                if self.bot_pos and self.princess_pos:
                    return
    
    def find_route(self):
        bot_row, bot_col = self.bot_pos
        princess_row, princess_col = self.princess_pos
        route = []

        while bot_row != princess_row:
            if bot_row < princess_row:
                route.append(self.down)
                bot_row += 1
            else:
                route.append(self.up)
                bot_row -= 1
        
        while bot_col != princess_col:
            if bot_col < princess_col:
                route.append(self.right)
                bot_col += 1
            else:
                route.append(self.left)
                bot_col -= 1

        return route


def displayPathtoPrincess(grid_size, grid):
    find_the_princess = FindThePrincess(grid_size, grid)
    for instruction in find_the_princess.find_route():
        print(instruction)


if __name__ == "__main__":
    gs = 3
    grid = ["---", "-m-", "--p"]
    displayPathtoPrincess(gs, grid)