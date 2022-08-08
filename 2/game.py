# The goal is to create a mine-sweeper board with the given number of cols, rows, and mines
# The board should use "x" for mines and each square should contain the number of adjacent mines
# (consider squares in both cardinal and ordinal directions)

# For example, a 3x3 board with 3 mines should look something like:
# 1 2 2
# 1 x x
# 1 3 x

from typing import List, Union, Tuple
from random import randint

Board = List[List[Union[str, int]]]
MineCoords = List[int]


def _gen_mine_coords(cols: int, rows: int, mines: int) -> MineCoords:
    if mines > cols * rows:
        raise RuntimeError("Too many mines...")

    mine_coords = []

    while len(mine_coords) < mines:
        col = randint(0, cols - 1)
        row = randint(0, rows - 1)
        coord = (col, row)
        if coord not in mine_coords:
            mine_coords.append(coord)

    return mine_coords


def _update_square(board: Board, col: int, row: int) -> Board:
    if col < 0 or row < 0:
        return board

    try:
        board[row][col] += 1
    except (IndexError, TypeError) as e:
        pass

    return board


def _update_neighbors(board: Board, col: int, row: int) -> Board:
    col_before = col - 1
    col_after = col + 1

    row_before = row - 1
    row_after = row + 1

    combos = (
            (col_before, row_before),
            (col_before, row),
            (col_before, row_after),

            (col, row_before),
            (col, row_after),

            (col_after, row_before),
            (col_after, row),
            (col_after, row_after),
            )

    for combo in combos:
        board = _update_square(board, combo[0], combo[1])

    return board


def _gen_board(cols: int, rows: int, mine_coords: MineCoords) -> Board:
    board = [[0 for col in range(cols)] for row in range(rows)]

    for mine in mine_coords:
        col = mine[0]
        row = mine[1]

        board[row][col] = 'x'
        board = _update_neighbors(board, col, row)

    return board


def create_board(cols: int, rows: int, mines: int):
    mine_coords = _gen_mine_coords(cols, rows, mines)
    board = _gen_board(cols, rows, mine_coords)
    for row in board:
        for col in row:
            print(col, end=' ')
        print()


create_board(3, 3, 3)
create_board(1, 10, 1)
create_board(11, 2, 1)
create_board(11, 2, 11)

