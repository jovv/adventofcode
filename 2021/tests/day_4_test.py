from days.day_4 import (bingo, draws, raw_boards, raw_to_board, Board, boards,
                        FIRST_COMPLETE_BOARD_WINS, LAST_COMPLETE_BOARD_WINS)
from days.inputreader import day_input, day

expected_draws = [
    '7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21', '24', '10',
    '16', '13', '6', '15', '25', '12', '22', '18', '20', '8', '19', '3', '26',
    '1'
]

expected_2d = [
    [
        ['22', '13', '17', '11', '0'],
        ['8', '2', '23', '4', '24'],
        ['21', '9', '14', '16', '7'],
        ['6', '10', '3', '18', '5'],
        ['1', '12', '20', '15', '19'],
    ],
    [
        ['3', '15', '0', '2', '22'],
        ['9', '18', '13', '17', '5'],
        ['19', '8', '7', '25', '23'],
        ['20', '11', '10', '24', '4'],
        ['14', '21', '16', '12', '6'],
    ],
    [
        ['14', '21', '17', '24', '4'],
        ['10', '16', '15', '9', '19'],
        ['18', '8', '23', '26', '20'],
        ['22', '11', '13', '6', '5'],
        ['2', '0', '12', '3', '7'],
    ],
]

expected_raw_boards = [
    [
        '22 13 17 11  0\n',
        ' 8  2 23  4 24\n',
        '21  9 14 16  7\n',
        ' 6 10  3 18  5\n',
        ' 1 12 20 15 19\n',
    ],
    [
        ' 3 15  0  2 22\n',
        ' 9 18 13 17  5\n',
        '19  8  7 25 23\n',
        '20 11 10 24  4\n',
        '14 21 16 12  6\n',
    ],
    [
        '14 21 17 24  4\n',
        '10 16 15  9 19\n',
        '18  8 23 26 20\n',
        '22 11 13  6  5\n',
        ' 2  0 12  3  7\n',
    ],
]

expected_marked_board = [
    ['22', '13', '17', '11', '0'],
    ['8', '2', '23', '4', '24'],
    ['21', '9', '14', '16', 'x'],
    ['6', '10', '3', '18', '5'],
    ['1', '12', '20', '15', '19'],
]

test_input = day_input(f'{day(__file__)}_input.txt')


def test_draws():
    assert draws(test_input) == expected_draws


def test_raw_boards():
    assert raw_boards(test_input[2:]) == expected_raw_boards


def test_raw_to_board():
    assert raw_to_board(expected_raw_boards[0]) == expected_2d[0]


def test_mark_board():
    expected_marked_board = [
        ['22', '13', '17', '11', '0'],
        ['8', '2', '23', '4', '24'],
        ['21', '9', '14', '16', 'x'],
        ['6', '10', '3', '18', '5'],
        ['1', '12', '20', '15', '19'],
    ]

    board = Board(expected_2d[0])
    board.mark('7')

    assert board.get() == expected_marked_board


def test_complete_row():
    board_1 = Board([
        ['22', '13', '17', '11', '0'],
        ['8', '2', '23', '4', '24'],
        ['x', 'x', 'x', 'x', 'x'],
        ['6', '10', '3', '18', '5'],
        ['1', '12', '20', '15', '19'],
    ])

    board_2 = Board([
        ['22', '13', '17', '11', '0'],
        ['x', '2', 'x', '4', '24'],
        ['21', 'x', 'x', 'x', 'x'],
        ['6', '10', 'x', '18', '5'],
        ['1', '12', '20', '15', '19'],
    ])

    assert Board.has_complete_row(board_1) == True
    assert Board.has_complete_row(board_2) == False
    assert Board.has_complete_row(Board(expected_2d[0])) == False


def test_complete_column():

    board_1 = Board([
        ['22', '13', '17', '11', '0'],
        ['8', '2', '23', '4', '24'],
        ['21', 'x', 'x', 'x', 'x'],
        ['6', '10', '3', '18', '5'],
        ['1', '12', '20', '15', '19'],
    ])

    board_2 = Board([
        ['22', '13', 'x', '11', '0'],
        ['x', '2', 'x', '4', '24'],
        ['21', 'x', 'x', 'x', 'x'],
        ['6', '10', 'x', '18', '5'],
        ['1', '12', 'x', '15', '19'],
    ])

    assert Board.has_complete_column(board_1) == False
    assert Board.has_complete_column(board_2) == True
    assert Board.has_complete_column(Board(expected_2d[0])) == False


def test_sum_unmarked():

    board = Board([
        ['22', '13', 'x', '11', '0'],
        ['x', '2', 'x', '4', '24'],
        ['21', 'x', 'x', 'x', 'x'],
        ['6', '10', 'x', '18', '5'],
        ['1', '12', 'x', '15', '19'],
    ])

    assert board.sum_unmarked() == 183


def test_equality():
    a = Board(expected_2d[0])
    b = Board(expected_2d[0])
    c = Board(expected_2d[1])

    assert a == b
    assert a != c


def test_boards():

    for i, board in enumerate(boards(test_input)):
        board == Board(expected_2d[i])


def test_bingo_first_win():

    assert bingo(expected_draws, boards(test_input),
                 FIRST_COMPLETE_BOARD_WINS) == 4512


def test_bingo_last_win():

    assert bingo(expected_draws, boards(test_input),
                 LAST_COMPLETE_BOARD_WINS) == 1924
