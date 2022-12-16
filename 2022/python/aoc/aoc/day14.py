import functools
import itertools
from typing import List, Tuple

ROCK = "#"
AIR = "."
SAND = "o"

Grid = List[List[str]]
Point = Tuple[int, int]
Pairs = List[List[Tuple[Point, Point]]]


def cave_rocks(grid: Grid, rocks: Pairs) -> Grid:
    for rock in rocks:
        for bounds in rock:
            start, end = bounds
            if start > end:
                start, end = end, start
            if start[0] == end[0]:
                x = start[0]
                for y in range(start[1], end[1] + 1):
                    grid[y][x] = ROCK
            elif start[1] == end[1]:
                y = start[1]
                for x in range(start[0], end[0] + 1):
                    grid[y][x] = ROCK

    return grid


def show_cave(cave: Grid):
    with open("cave.txt", "w") as f:
        for row in cave:
            f.write("".join(row) + "\n")


def drop_sand(cave: Grid, y_max: int, part: int) -> int:
    n = 0
    while True:  # not bothering with recursion in Python
        origin = (500, 0)
        x, y = origin
        if part == 2 and cave[y][x] == SAND:
            break
        while True:
            if y >= y_max:
                break
            if cave[y + 1][x] == AIR:
                y += 1
            elif cave[y + 1][x - 1] == AIR:
                y += 1
                x -= 1
            elif cave[y + 1][x + 1] == AIR:
                y += 1
                x += 1
            else:
                break
        if y >= y_max:
            break
        n += 1
        cave[y][x] = SAND
    # show_cave(cave)
    return n


def add_cave_floor(cave: Grid, x_max: int) -> Grid:
    return cave + [[AIR] * x_max, [ROCK] * x_max]


def part1(rocks: List[List[Tuple[int, int]]], x_max: int, y_max: int) -> int:

    grid = [[AIR for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    # rock start-end pairs
    pairs = [list(itertools.pairwise(rock)) for rock in rocks]

    cave = cave_rocks(grid, pairs)

    units_of_sand = drop_sand(cave, y_max, 1)

    return units_of_sand


def part2(rocks: List[List[Tuple[int, int]]], x_max: int, y_max: int) -> int:

    cave_width = (x_max * 2) + 1
    grid = add_cave_floor(
        [[AIR for _ in range(cave_width + 1)] for _ in range(y_max + 1)],
        cave_width + 1,
    )

    # rock start-end pairs
    pairs = [list(itertools.pairwise(rock)) for rock in rocks]

    cave = cave_rocks(grid, pairs)

    show_cave(cave)

    units_of_sand = drop_sand(cave, y_max + 2, 2)

    return units_of_sand


if __name__ == "__main__":

    FILENAME = "day14.txt"
    with open(FILENAME) as f:
        content = [line.strip() for line in f.readlines()]

    coords = [[tuple(map(int, coord.split(","))) for coord in line.split(" -> ")] for line in content]

    # cave boundaries
    x_bound, y_bound = functools.reduce(
        lambda start, end: (max(start[0], end[0]), max(start[1], end[1])),
        (tup for rock in coords for tup in rock),
        (-1, -1),
    )

    print(f"Part 1: {part1(coords, x_bound, y_bound)}")
    print(f"Part 2: {part2(coords, x_bound, y_bound)}")
