from typing import List, Tuple

NEIGHBOURS = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
]

SIDES = 6


def surface_area(coords: List[Tuple[int, int, int]]) -> int:

    cnt = 0
    cubes = set()
    for coord in coords:
        cnt += SIDES
        if coord in cubes:
            continue
        cubes.add(coord)

        for neighbour in NEIGHBOURS:
            check = tuple(a + b for a, b in zip(coord, neighbour))
            if check in cubes:
                cnt -= 2

    return cnt


if __name__ == "__main__":

    FILENAME = "day18.txt"
    with open(FILENAME) as f:
        content = [line.strip() for line in f.readlines()]

    droplets = [tuple(map(int, line.split(","))) for line in content]

    print(f"Part 1: {surface_area(droplets)}")
    # print(f"Part 2: {}", 0)
