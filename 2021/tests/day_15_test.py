import numpy as np

from days.day_15 import initialize, shortest_path

small = np.array([
    [1, 1, 6],
    [1, 3, 8],
    [2, 1, 3],
])


def test_shortest_path_small():
    g, u, c = initialize(small)
    assert shortest_path(g, u, c, (0, 0), (2, 2)) == 7
