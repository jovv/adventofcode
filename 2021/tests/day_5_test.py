from days.day_5 import (diagonal_range, to_positive_vector, vectors, vents,
                        Vector)

test_input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]

expected_vectors = [
    Vector([[0, 9], [5, 9]]),
    Vector([[8, 0], [0, 8]]),
    Vector([[9, 4], [3, 4]]),
    Vector([[2, 2], [2, 1]]),
    Vector([[7, 0], [7, 4]]),
    Vector([[6, 4], [2, 0]]),
    Vector([[0, 9], [2, 9]]),
    Vector([[3, 4], [1, 4]]),
    Vector([[0, 0], [8, 8]]),
    Vector([[5, 5], [8, 2]]),
]

orientation_testcases = [
    Vector([[0, 9], [5, 9]]),
    Vector([[8, 0], [0, 8]]),
    Vector([[2, 2], [2, 1]]),
]


def test_vector():
    vec = Vector([[1, 2], [3, 4]])
    assert vec.x1 == 1
    assert vec.x2 == 3
    assert vec.y1 == 2
    assert vec.y2 == 4


def test_vector_repr():
    vec = Vector([[1, 2], [3, 4]])
    assert str(vec) == 'Vector((1, 2), (3, 4))'


def test_vector_equality():
    vec1 = Vector([[1, 2], [3, 4]])
    vec2 = Vector([[1, 2], [3, 4]])

    assert vec1 == vec2


def test_vectors():

    assert vectors(test_input) == expected_vectors


def test_is_horizontal():

    expected = [True, False, False]
    for test in zip(orientation_testcases, expected):
        assert test[0].is_horizontal() == test[1]


def test_is_vertical():

    expected = [False, False, True]
    for test in zip(orientation_testcases, expected):
        assert test[0].is_vertical() == test[1]


def test_is_diagonal():

    expected = [False, True, False]
    for test in zip(orientation_testcases, expected):
        assert test[0].is_diagonal() == test[1]


def test_direction():
    testcases = [
        {
            'input': Vector([[1, 1], [1, 5]]),
            'expected': 1
        },
        {
            'input': Vector([[1, 1], [5, 1]]),
            'expected': 1
        },
        {
            'input': Vector([[5, 1], [1, 1]]),
            'expected': -1
        },
        {
            'input': Vector([[1, 5], [1, 1]]),
            'expected': -1
        },
        {
            'input': Vector([[1, 1], [3, 3]]),
            'expected': (1, 1)
        },
        {
            'input': Vector([[7, 9], [9, 7]]),
            'expected': (1, -1)
        },
        {
            'input': Vector([[5, 3], [3, 5]]),
            'expected': (-1, 1)
        },
        {
            'input': Vector([[5, 5], [3, 3]]),
            'expected': (-1, -1)
        },
    ]

    for test in testcases:
        assert test['input'].direction() == test['expected']


def test_to_positive_vector():
    testcases = [{
        'input': Vector([[0, 9], [5, 9]]),
        'expected': Vector([[0, 9], [5, 9]]),
    }, {
        'input': Vector([[9, 4], [3, 4]]),
        'expected': Vector([[3, 4], [9, 4]]),
    }, {
        'input': Vector([[2, 2], [2, 1]]),
        'expected': Vector([[2, 1], [2, 2]]),
    }, {
        'input': Vector([[7, 0], [7, 4]]),
        'expected': Vector([[7, 0], [7, 4]]),
    }, {
        'input': Vector([[0, 9], [2, 9]]),
        'expected': Vector([[0, 9], [2, 9]]),
    }, {
        'input': Vector([[3, 4], [1, 4]]),
        'expected': Vector([[1, 4], [3, 4]]),
    }, {
        'input': Vector([[5, 5], [3, 3]]),
        'expected': Vector([[3, 3], [5, 5]]),
    }, {
        'input': Vector([[5, 3], [3, 5]]),
        'expected': Vector([[3, 5], [5, 3]]),
    }]

    for test in testcases:
        assert to_positive_vector(test['input']) == test['expected']


def test_diagonal_range():

    testcases = [
        {
            'input': Vector([[1, 1], [3, 3]]),
            'expected': [(1, 1), (2, 2), (3, 3)]
        },
        {
            'input': Vector([[7, 9], [9, 7]]),
            'expected': [(7, 9), (8, 8), (9, 7)]
        },
    ]

    for test in testcases:
        assert diagonal_range(test['input']) == test['expected']


def test_horizontal_and_vertical_vents():

    assert vents(
        to_positive_vector(vec) for vec in expected_vectors
        if not vec.is_diagonal()) == 5


def test_all_vents():

    assert vents(to_positive_vector(vec) for vec in expected_vectors) == 12
