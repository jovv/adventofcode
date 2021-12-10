from functools import reduce
from typing import List, Tuple

import numpy as np
from scipy import ndimage as ndi

from days.inputreader import day_input, day


def content_to_heightmap(content: List[List[str]]) -> List[List[int]]:
    return [[int(s) for s in list(line.strip())] for line in content]


def total_risk_level(low_points: List[int]) -> List[int]:
    return sum([pt[1] + 1 for pt in low_points])


def adjacent_locations(heights: List[List[int]], row_i: int,
                       col_i: int) -> List[int]:
    row_len = len(heights)
    col_len = len(heights[0])
    locs = []
    # top left
    if row_i == 0 and col_i == 0:
        locs = [
            heights[row_i][col_i + 1],
            heights[row_i + 1][col_i],
        ]
    # top right
    elif row_i == 0 and col_i == col_len - 1:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i + 1][col_i],
        ]
    # bottom left
    elif row_i == row_len - 1 and col_i == 0:
        locs = [
            heights[row_i][col_i + 1],
            heights[row_i - 1][col_i],
        ]
    # bottom right
    elif row_i == row_len - 1 and col_i == col_len - 1:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i - 1][col_i],
        ]
    # left edge
    elif col_i == 0:
        locs = [
            heights[row_i][col_i + 1],
            heights[row_i - 1][col_i],
            heights[row_i + 1][col_i],
        ]
    # right edge
    elif col_i == col_len - 1:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i - 1][col_i],
            heights[row_i + 1][col_i],
        ]
    # top edge
    elif row_i == 0:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i][col_i + 1],
            heights[row_i + 1][col_i],
        ]
    # bottom edge
    elif row_i == row_len - 1:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i][col_i + 1],
            heights[row_i - 1][col_i],
        ]
    # regular case, no edges
    else:
        locs = [
            heights[row_i][col_i - 1],
            heights[row_i][col_i + 1],
            heights[row_i - 1][col_i],
            heights[row_i + 1][col_i],
        ]
    return locs


def low_points(heightmap: List[List[int]]) -> List[Tuple[Tuple[int, int], int]]:
    low_pts = []
    for r, row in enumerate(heightmap):
        for c, height in enumerate(row):
            adj_xs = adjacent_locations(heightmap, r, c)
            if height < min(adj_xs):
                low_pts.append(((r, c), height))

    return low_pts


def top_3_basins(heightmap: np.ndarray) -> int:
    basins, nr_of_basins = ndi.label(heightmap < 9)
    basin_sizes = [(basins == i + 1).sum() for i in range(nr_of_basins)]
    return reduce(lambda a, b: a * b, sorted(basin_sizes, reverse=True)[0:3])


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    heightmap = content_to_heightmap(content)

    part1 = total_risk_level(low_points(heightmap))
    np_heightmap = np.array(heightmap)
    part2 = top_3_basins(np_heightmap)

    print(part1)
    print(part2)
