from days.inputreader import day_input, day
from typing import List

FORWARD = 'forward'
UP = 'up'
DOWN = 'down'


def position(movements: List[str]) -> int:
    horizontal = 0
    vertical = 0

    for movement in movements:
        direction, magnitude = movement.split(' ')
        magnitude = int(magnitude)
        if direction == FORWARD:
            horizontal += magnitude
        elif direction == UP:
            vertical -= magnitude
        elif direction == DOWN:
            vertical += magnitude
        else:
            raise ValueError(f'{direction} is not a valid direction')

    return horizontal * vertical


def position_with_aim(movements: List[str]) -> int:

    horizontal = 0
    vertical = 0
    aim = 0

    for movement in movements:
        direction, magnitude = movement.split(' ')
        magnitude = int(magnitude)
        if direction == FORWARD:
            horizontal += magnitude
            vertical += aim * magnitude
        elif direction == UP:
            aim -= magnitude
        elif direction == DOWN:
            aim += magnitude
        else:
            raise ValueError(f'{direction} is not a valid direction')

    return horizontal * vertical


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    lines = [line for line in content]

    part1 = position(lines)
    part2 = position_with_aim(lines)

    print(part1)
    print(part2)
