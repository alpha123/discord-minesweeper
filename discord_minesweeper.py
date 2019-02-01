import math
import random
import sys

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_board(nrows, ncols, nbombs):
    """Generates a minesweeper board as an array of arrays of numbers. -1 is a bomb,
       0 is empty, and positive numbers are the number of adjacent bombs.
    """
    bombs = []
    for i in range(nbombs):
        bomb_valid = False
        new_bomb = Bomb(-1,-1)
        while not bomb_valid:
            new_bomb.x = math.floor(random.random() * nrows)
            new_bomb.y = math.floor(random.random() * ncols)
            bomb_valid = all(map(lambda b: b.x != new_bomb.x and b.y != new_bomb.y, bombs))
        bombs.append(new_bomb)

    grid = [[0] * ncols for _ in range(nrows)]
    for r in range(nrows):
        for c in range(ncols):
            contains_bomb = any(map(lambda b: b.x == r and b.y == c, bombs))
            if contains_bomb:
                grid[r][c] = -1
            else:
                nadjacent = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        nadjacent += sum(map(lambda b: 1 if b.x == i and b.y == j else 0, bombs))
                grid[r][c] = nadjacent
    return grid

def board_to_discord(grid, empty=':__:'):
    """Turn a board from `generate_board` into a message using Discord
       spoilers and emoji. The `empty` parameter is what
       representation should be used for an empty square.
    """
    REPR = [':bomb:', empty, ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:']
    return '\n'.join(''.join(map(lambda n: REPR[n+1], row)) for row in grid)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Syntax: {} nrows ncols nbombs".format(sys.argv[0]))
        quit()
    try:
        nrows = int(sys.argv[1])
        ncols = int(sys.argv[2])
        nbombs = int(sys.argv[3])
    except ValueError:
        print("Syntax: {} nrows ncols nbombs".format(sys.argv[0]))
        quit()
    print(board_to_discord(generate_board(nrows, ncols, nbombs)))
