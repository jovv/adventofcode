import numpy as np

from days.day_9 import (adjacent_locations, content_to_heightmap, low_points,
                        total_risk_level, top_3_basins)

sample_input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

sample_heightmap = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


def test_adjacent_locations():
    sample_heightmap = [
        [2, 1, 9, 1, 0],
        [3, 9, 8, 2, 1],
        [9, 8, 5, 9, 2],
    ]

    testcases = [
        [(1, 1), [3, 8, 1, 8]],  # regular case, no edges
        [(0, 0), [1, 3]],  # top left
        [(0, 4), [1, 1]],  # top right
        [(2, 0), [8, 3]],  # bottom left
        [(2, 4), [9, 1]],  # bottom right
        [(1, 0), [9, 2, 9]],  # left edge
        [(1, 4), [2, 0, 2]],  # right edge
        [(2, 2), [8, 9, 8]],  # bottom edge
        [(0, 2), [1, 1, 8]],  # top edge
    ]

    for test in testcases:
        r, c = test[0]
        expected = test[1]
        assert adjacent_locations(sample_heightmap, r, c) == expected


def test_total_risk_level():
    low_pts = [
        ((0, 1), 1),
        ((0, 9), 0),
        ((2, 2), 5),
        ((4, 6), 5),
    ]
    assert total_risk_level(low_pts) == 15


def test_low_pts():
    assert low_points(sample_heightmap) == [
        ((0, 1), 1),
        ((0, 9), 0),
        ((2, 2), 5),
        ((4, 6), 5),
    ]


def test_heightmap():

    assert content_to_heightmap(sample_input) == sample_heightmap


def test_top_3_basins():
    np_heightmap = np.array(sample_heightmap)
    assert top_3_basins(np_heightmap) == 1134
