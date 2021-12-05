from collections import Counter
from typing import List, Tuple, Union

from days.inputreader import day_input, day


class Vector():

    def __init__(self, raw: List[List[int]]) -> None:
        self.x1, self.y1 = raw[0]
        self.x2, self.y2 = raw[1]

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_diagonal(self) -> bool:
        return not (self.is_horizontal() or self.is_vertical())

    def direction(self) -> Union[int, Tuple[int, int]]:
        if self.is_horizontal():
            return -1 if self.x1 > self.x2 else 1
        elif self.is_vertical():
            return -1 if self.y1 > self.y2 else 1
        else:
            return (-1 if self.x1 > self.x2 else 1,
                    -1 if self.y1 > self.y2 else 1)

    def __eq__(self, other) -> bool:
        return (self.x1 == other.x1 and self.x2 == other.x2 and
                self.y1 == other.y1 and self.y2 == other.y2)

    def __repr__(self) -> str:
        return f'Vector(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))'


def vectors(lines) -> List[List[Tuple[int, int]]]:
    return [
        Vector([[int(s) for s in coord.strip().split(',')]
                for coord in line.strip().split('->')]) for line in lines
    ]


def to_positive_vector(vec: Vector) -> Vector:
    """    
    Flip vectors to positive orientation.
    For diagonals, flip to positive x.
    The intention is to simplify coordinate calculation by going left to right 
        only on at least the x-axis.
    """
    if vec.is_horizontal() and vec.direction() == -1:
        vec.x1, vec.x2 = vec.x2, vec.x1
    elif vec.is_vertical() and vec.direction() == -1:
        vec.y1, vec.y2 = vec.y2, vec.y1
    elif vec.is_diagonal() and vec.direction()[0] == -1:
        vec.x1, vec.x2 = vec.x2, vec.x1
        vec.y1, vec.y2 = vec.y2, vec.y1

    return vec


def diagonal_range(vec: Vector):
    x_dir, y_dir = vec.direction()
    if x_dir == 1:
        return list(
            zip(
                range(vec.x1, vec.x2 + x_dir, x_dir),
                range(vec.y1, vec.y2 + y_dir, y_dir)))
    else:
        raise ValueError('Accepts vectors with positive x direction only')


def vents(vecs: List[Vector]) -> int:
    coordinates = []
    for vec in vecs:
        if vec.is_vertical():
            coordinates += [(vec.x1, y) for y in range(vec.y1, vec.y2 + 1, 1)]
        elif vec.is_horizontal():
            coordinates += [(x, vec.y1) for x in range(vec.x1, vec.x2 + 1, 1)]
        else:
            coordinates += diagonal_range(vec)

    return len(
        list(coord for coord, cnt in Counter(coordinates).items() if cnt != 1))


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    all_vectors = vectors(content)
    positive_nondiagonal_vectors = [
        to_positive_vector(vec) for vec in all_vectors if not vec.is_diagonal()
    ]
    positive_vectors = [to_positive_vector(vec) for vec in all_vectors]

    part1 = vents(positive_nondiagonal_vectors)
    part2 = vents(positive_vectors)

    print(part1)
    print(part2)
