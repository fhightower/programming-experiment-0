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
MineCoords = List[Tuple[int, int]]


def _gen_board(cols: int, rows: int) -> Board:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def _get_mine_coords(board: Board, cols: int, rows: int, mines: int) -> MineCoords:
    if mines > cols * rows:
        msg = "There will be a problem as you want more mines than there are squares"
        raise RuntimeError(msg)

    mine_coords = []
    while len(mine_coords) < mines:
        col = randint(0, cols - 1)
        row = randint(0, rows - 1)
        coords = (col, row)
        if coords not in mine_coords:
            mine_coords.append(coords)

    return mine_coords


def _update_square(board: Board, col: int, row: int) -> Board:
    if col < 0 or row < 0:
        return board

    try:
        board[row][col] += 1
    # IndexError occurs when the row, col doesn't exist on the board...
    # TypeError occurs when the neighbor is a mine
    except (IndexError, TypeError):
        pass

    return board


def _update_neighbors(board: Board, col: int, row: int) -> Board:
    col_before = col - 1
    col_after = col + 1

    row_before = row - 1
    row_after = row + 1

    board = _update_square(board, col_before, row_before)
    board = _update_square(board, col_before, row)
    board = _update_square(board, col_before, row_after)

    board = _update_square(board, col, row_before)
    board = _update_square(board, col, row_after)

    board = _update_square(board, col_after, row_before)
    board = _update_square(board, col_after, row)
    board = _update_square(board, col_after, row_after)

    return board


def _apply_mine_coords(board: Board, mine_coords: MineCoords) -> Board:
    for coords in mine_coords:
        col = coords[0]
        row = coords[1]

        board[row][col] = 'x'
        board = _update_neighbors(board, col, row)
    return board


def create_board(cols: int, rows: int, mines: int) -> Board:
    board = _gen_board(cols, rows)
    mine_coords = _get_mine_coords(board, cols, rows, mines)
    board = _apply_mine_coords(board, mine_coords)

    for row in board:
        for col in row:
            print(col, end=' ')
        print()

    return board


create_board(3, 3, 3)
create_board(1, 10, 1)
create_board(11, 2, 1)
create_board(11, 2, 11)

