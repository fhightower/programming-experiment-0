# The goal is to create a mine-sweeper board with the given number of cols, rows, and mines
# The board should use "x" for mines and each square should contain the number of adjacent mines
# (consider squares in both cardinal and ordinal directions)

# For example, a 3x3 board with 3 mines should look something like:
# 1 2 2
# 1 x x
# 1 3 x

from typing import List, Union
from random import randint

MINE_SYMBOL = "x"
Board = List[List[Union[int, str]]]


def _gen_board(cols: int, rows: int):
    return [[0 for c in range(cols)] for r in range(rows)]


def _inc_square(board: Board, col: int, row: int):
    """Try to increment the value in the given col and row.

    Will handle failures b/c neighbor is a mine or b/c neighbor DNE (the coordinates are off the board)"""
    if col < 0 or row < 0:
        return board

    try:
        board[row][col] += 1
    except (IndexError, TypeError) as e:
        pass
    return board


def _update_neighbors(board: Board, mine_col: int, mine_row: int):
    col_before = mine_col - 1
    col_after = mine_col + 1

    row_before = mine_row - 1
    row_after = mine_row + 1

    # update the previous column
    board = _inc_square(board, col_before, row_before)
    board = _inc_square(board, col_before, mine_row)
    board = _inc_square(board, col_before, row_after)

    # update the mine_col
    board = _inc_square(board, mine_col, row_before)
    board = _inc_square(board, mine_col, row_after)

    # update the next column
    board = _inc_square(board, col_after, row_before)
    board = _inc_square(board, col_after, mine_row)
    board = _inc_square(board, col_after, row_after)

    return board


def _add_mines(board: Board, cols: int, rows: int, mines: int):
    for mine in range(mines):
        while True:
            col_index = randint(0, cols - 1)
            row_index = randint(0, rows - 1)
            if board[row_index][col_index] != MINE_SYMBOL:
                board[row_index][col_index] = MINE_SYMBOL
                board = _update_neighbors(board, col_index, row_index)
                break
    return board


def create_board(cols: int, rows: int, mines: int):
    board = _gen_board(cols, rows)
    board = _add_mines(board, cols, rows, mines)
    for row in board:
        for i in row:
            print(i, end=' ')
        print('')
    return board


create_board(3, 3, 3)
print()
create_board(1, 3, 1)
print()
create_board(11, 2, 1)
print()
create_board(11, 2, 11)

