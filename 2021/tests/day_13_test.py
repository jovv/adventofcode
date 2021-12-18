import numpy as np

from days.day_13 import fold_grid, parse_content, to_grid, nr_of_dots, grid_shape

sample_content = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]

expected_grid: np.ndarray = np.array([
    [6, 10],
    [0, 14],
    [9, 10],
    [0, 3],
    [10, 4],
    [4, 11],
    [6, 0],
    [6, 12],
    [4, 1],
    [0, 13],
    [10, 12],
    [3, 4],
    [3, 0],
    [8, 4],
    [1, 10],
    [2, 14],
    [8, 10],
    [9, 0],
])

expected_folds = [('y', 7), ('x', 5)]


def test_parse_content():

    grid, folds = parse_content(sample_content)
    assert np.array_equal(grid, expected_grid)
    assert folds == expected_folds


def test_grid_shape():
    assert grid_shape(expected_grid) == (15, 11)


def test_nr_of_dots():
    assert nr_of_dots(
        fold_grid(
            grid=to_grid(expected_grid, grid_shape(expected_grid)),
            folds=expected_folds,
            stop=True,
        )) == 17
