from days.day_2 import position, position_with_aim

input = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]


def test_position():

    testcases = [(input, 150)]
    for test in testcases:
        assert position(test[0]) == test[1]


def test_position_with_aim():

    testcases = [(input, 900)]
    for test in testcases:
        assert position_with_aim(test[0]) == test[1]
