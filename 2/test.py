import pytest

from game import _gen_board, _get_mine_coords, _apply_mine_coords, _update_neighbors


def test_update_neighbors():
    board = [[0, 0, 0], [0, 0, 'x']]
    board = _update_neighbors(board, 2, 1)
    assert board == [[0, 1, 1], [0, 1, 'x']]


def test_gen_board():
    rows = 1
    cols = 1
    board = _gen_board(cols, rows)
    assert len(board) == rows
    assert len(board[0]) == cols

    rows = 5
    cols = 4
    board = _gen_board(cols, rows)
    assert len(board) == rows
    assert len(board[0]) == cols

    rows = 3
    cols = 10
    board = _gen_board(cols, rows)
    assert len(board) == rows
    assert len(board[0]) == cols


def test_get_mine_coords():
    rows = 3
    cols = 3
    mines = 3
    board = _gen_board(cols, rows)
    mine_coords = _get_mine_coords(board, cols, rows, mines)
    assert len(mine_coords) == mines

    rows = 1
    cols = 1
    mines = 3
    board = _gen_board(cols, rows)
    with pytest.raises(RuntimeError):
        mine_coords = _get_mine_coords(board, cols, rows, mines)


def test_apply_mine_coords():
    rows = 3
    cols = 3
    mines = 3
    board = _gen_board(cols, rows)
    mine_coords = _get_mine_coords(board, cols, rows, mines)
    board = _apply_mine_coords(board, mine_coords)
    mine_count = 0

    for row in board:
        for col in row:
            if col == 'x':
                mine_count += 1

    assert mine_count == mines

