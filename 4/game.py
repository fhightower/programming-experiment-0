# The goal is to create a mine-sweeper board with the given number of cols, rows, and mines
# The board should use "x" for mines and each square should contain the number of adjacent mines
# (consider squares in both cardinal and ordinal directions)

# For example, a 3x3 board with 3 mines should look something like:
# 1 2 2
# 1 x x
# 1 3 x

from random import randint
from typing import List, Union

Board = List[List[Union[int, str]]]


def _gen_board(cols: int, rows: int) -> Board:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def _update_neighbor(board: Board, col: int, row: int) -> Board:
    if col < 0 or row < 0:
        return board

    try:
        board[row][col] += 1
    except (TypeError, IndexError):
        pass

    return board


def _update_neighbors(board: Board, mine_col: int, mine_row: int) -> Board:
    col_before = mine_col - 1
    col_after = mine_col + 1

    row_before = mine_row - 1
    row_after = mine_row + 1

    board = _update_neighbor(board, col_before, row_before)
    board = _update_neighbor(board, col_before, mine_row)
    board = _update_neighbor(board, col_before, row_after)

    board = _update_neighbor(board, mine_col, row_before)
    board = _update_neighbor(board, mine_col, row_after)

    board = _update_neighbor(board, col_after, row_before)
    board = _update_neighbor(board, col_after, mine_row)
    board = _update_neighbor(board, col_after, row_after)

    return board


def _place_mine(board: Board, cols: int, rows: int) -> Board:
    while True:
        mine_col = randint(0, cols - 1)
        mine_row = randint(0, rows - 1)

        # if the randomly selected square is not already a mine
        if board[mine_row][mine_col] != 'x':
            board[mine_row][mine_col] = 'x'
            board = _update_neighbors(board, mine_col, mine_row)
            break
    return board


def _place_mines(board: Board, cols: int, rows: int, mines: int) -> Board:
    if mines > cols * rows:
        raise RuntimeError("Too many mines...")

    mines_placed = 0
    while mines_placed < mines:
        board = _place_mine(board, cols, rows)
        mines_placed += 1

    return board


def create_board(cols: int, rows: int, mines: int):
    board = _gen_board(cols, rows)
    board = _place_mines(board, cols, rows, mines)

    for row in board:
        for col in row:
            print(col, end=' ')
        print()


create_board(3, 3, 3)
create_board(1, 10, 1)
create_board(11, 2, 1)
create_board(11, 2, 11)

