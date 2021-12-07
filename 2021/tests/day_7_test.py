from days.day_6 import initial_state
from days.day_7 import align, FUEL_BURN_RATE_CONSTANT, FUEL_BURN_RATE_INCREASING, fuel_burn

content = ['16,1,2,0,4,2,7,1,2,14']
positions = initial_state(content)


def test_fuel_burn_constant():
    testcases = [
        ((16, 2, FUEL_BURN_RATE_CONSTANT), 14),
        ((0, 2, FUEL_BURN_RATE_CONSTANT), 2),
    ]

    for test in testcases:
        args, expected = test
        assert fuel_burn(*args) == expected


def test_fuel_burn_increasing():
    testcases = [
        ((16, 5, FUEL_BURN_RATE_INCREASING), 66),
        ((0, 5, FUEL_BURN_RATE_INCREASING), 15),
    ]

    for test in testcases:
        args, expected = test
        assert fuel_burn(*args) == expected


def test_align_by_constant_rate():
    assert align(positions, FUEL_BURN_RATE_CONSTANT) == 37


def test_align_by_increasing_rate():
    assert align(positions, FUEL_BURN_RATE_INCREASING) == 168
