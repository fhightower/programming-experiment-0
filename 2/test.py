import pytest

from game import _gen_mine_coords, _gen_board


def test_gen_mine_coords():
    results = _gen_mine_coords(3, 3, 1)
    assert len(results) == 1

    results = _gen_mine_coords(3, 3, 6)
    assert len(results) == 6

    results = _gen_mine_coords(3, 3, 9)
    assert len(results) == 9

    with pytest.raises(RuntimeError):
        results = _gen_mine_coords(3, 3, 10)


def test_gen_board():
    coords = _gen_mine_coords(1, 1, 1)
    board = _gen_board(1, 1, coords)
    assert board == [['x']]

    coords = _gen_mine_coords(2, 1, 1)
    board = _gen_board(2, 1, coords)
    assert len(board) == 1
    assert 'x' in board[0]
    assert 1 in board[0]

