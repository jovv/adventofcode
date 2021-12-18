from typing import List, Tuple
import numpy as np

from days.inputreader import day, day_input


def parse_content(
        content: List[str]) -> Tuple[np.ndarray, List[Tuple[str, int]]]:
    stripped = [s.strip() for s in content]
    slice_i = stripped.index('')
    coords = np.array(
        [[int(n) for n in s.split(',')] for s in stripped[:slice_i]])
    folds = [
        tuple([
            v if i == 0 else int(v)
            for i, v in enumerate(s.strip('fold along ').split('='))
        ]) for s in stripped[slice_i + 1:]
    ]
    return coords, folds


def grid_shape(coords: np.ndarray) -> Tuple[int, int]:

    x_max, y_max = coords.max(axis=0)
    return y_max + 1, x_max + 1


def to_grid(coords: np.ndarray, shape: Tuple[int, int]) -> np.ndarray:

    grid = np.zeros(shape=shape)
    for coord in coords:
        x, y = coord
        grid[y][x] = 1
    return grid


# we don't always fold in half, but numpy requires matching dimensions,
# so we need to pad an array edge when necessary
def pad_edge(fold_upon, folding):
    if fold_upon.shape == folding.shape:
        return fold_upon, folding

    a_y, a_x = fold_upon.shape
    b_y, b_x = folding.shape

    y = max(a_y, b_y)
    x = max(a_x, b_x)

    if a_y != b_y:
        row = np.zeros((abs(a_y - b_y), x))
        if y != a_y:
            fold_upon = np.concatenate((fold_upon, row), axis=0)
        else:
            folding = np.concatenate((folding, row), axis=0)
    else:
        col = np.zeros((y, abs(a_x - b_x)))
        if x != a_x:
            fold_upon = np.concatenate((fold_upon, col), axis=1)
        else:
            folding = np.concatenate((folding, col), axis=1)

    return fold_upon, folding


def fold_grid(grid: np.ndarray, folds: Tuple[str, int],
              stop: bool) -> np.ndarray:
    for fold in folds:
        fold_axis, fold_line = fold
        if fold_axis == 'y':
            np_axis = 0
            fold_upon = grid[:fold_line, :]
            folding = grid[fold_line + 1:, :]
            fold_upon, folding = pad_edge(fold_upon, folding)
        else:
            np_axis = 1
            fold_upon = grid[:, :fold_line]
            folding = grid[:, fold_line + 1:]
            fold_upon, folding = pad_edge(fold_upon, folding)

        grid = fold_upon + np.flip(folding, axis=np_axis)

        if stop:
            break

    return grid


def nr_of_dots(grid: np.ndarray) -> int:
    return np.sum(grid > 0)


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    coords, folds = parse_content(content)
    grid = to_grid(coords, grid_shape(coords))

    part1_grid = fold_grid(grid, folds, stop=True)
    part1 = nr_of_dots(part1_grid)

    part2_grid = fold_grid(grid, folds, stop=False)

    print(part1)
    print(part2_grid)  # CAFJHZCK, after some manual cleanup
