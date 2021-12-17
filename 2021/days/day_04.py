from days.inputreader import day_input, day
from days.day_3 import transpose
from typing import List

MARK = 'x'
WIN = 5 * MARK
FIRST_COMPLETE_BOARD_WINS = 'first'
LAST_COMPLETE_BOARD_WINS = 'last'


class Board():

    def __init__(self, board: List[List[str]]):
        self.__board = board

    def mark(self, draw: str):
        self.__board = [
            [nr if nr != draw else MARK for nr in row] for row in self.__board
        ]

    def has_complete_row(cls) -> bool:
        for row in cls.get():
            if ''.join(row) == WIN:
                return True
        return False

    def has_complete_column(cls) -> bool:
        return Board.has_complete_row(Board(transpose(cls.get())))

    def sum_unmarked(self) -> int:
        return sum(int(nr) for row in self.__board for nr in row if nr != MARK)

    def get(self) -> List[List[str]]:
        return self.__board

    def __eq__(self, other) -> bool:
        return self.__board == other.get()


def draws(lines: List[str]) -> List[str]:
    return lines[0].strip().split(',')


def raw_to_board(board: List[str]) -> List[List[str]]:
    return [[nr.strip()
             for nr in row.strip().split(' ')
             if nr != '']
            for row in board]


def raw_boards(lines: List[str]) -> List[List[str]]:
    boards = []
    i = 0
    while i < len(lines):
        boards.append(lines[i:i + 5])
        i += 5 + 1
    return boards


def boards(lines: List[str]) -> List[Board]:
    return [Board(raw_to_board(raw)) for raw in raw_boards(lines[2:])]


def bingo(draws: List[int], boards: List[Board], mode: str) -> int:
    if mode not in [FIRST_COMPLETE_BOARD_WINS, LAST_COMPLETE_BOARD_WINS]:
        return ValueError(f'{mode} is not a valid mode of playing bingo')

    winners = {}
    nr_of_boards = len(boards)

    for i, draw in enumerate(draws):
        for board in boards:
            board.mark(draw)
        if i >= 4:
            for j, board in enumerate(boards):
                if Board.has_complete_row(board) or Board.has_complete_column(
                        board):
                    winners[j] = True
                    if mode == FIRST_COMPLETE_BOARD_WINS:
                        return int(draw) * board.sum_unmarked()
                    if len(winners) == nr_of_boards:
                        return int(draw) * board.sum_unmarked()

    return 0


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    all_draws = draws(content)
    all_boards = boards(content)

    part1 = bingo(all_draws, all_boards, FIRST_COMPLETE_BOARD_WINS)
    part2 = bingo(all_draws, all_boards, LAST_COMPLETE_BOARD_WINS)

    print(part1)
    print(part2)
