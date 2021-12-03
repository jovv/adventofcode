from days.day_3 import (
    life_support_rating,
    most_common,
    power_consumption,
    transpose,
)

input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def test_transpose():
    testcases = [([
        'abc',
        'def',
        'ghi',
    ], [
        'adg',
        'beh',
        'cfi',
    ])]

    for test in testcases:
        assert transpose(test[0]) == test[1]


def test_power_consumption():

    testcases = [(input, 198)]
    for test in testcases:
        assert power_consumption(test[0]) == test[1]


def test_most_common():
    testcases = [
        ('1100', ('1', '0')),
        ('11100', ('1', '0')),
        ('10010', ('0', '1')),
    ]

    for test in testcases:
        assert most_common(test[0]) == test[1]


def test_life_support_rating():

    testcases = [(input, 230)]
    for test in testcases:
        assert life_support_rating(test[0]) == test[1]