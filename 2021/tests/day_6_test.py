from collections import Counter
from days.day_6 import (fish_state_count, initial_state, NR_OF_DAYS_PART_1,
                        NR_OF_DAYS_PART_2, lanternfish_brute_force,
                        lanternfish_perf)

content = ['3,4,3,1,2']
fish = [3, 4, 3, 1, 2]

testcases_brute_force = [
    (2, 6),
    (4, 9),
    (18, 26),
    (NR_OF_DAYS_PART_1, 5934),
]


def test_initial_state():

    assert initial_state(content) == fish


def test_fish_state_count():
    expected = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}
    assert fish_state_count(Counter(fish)) == expected


def test_lanternfish_brute_force():

    for test in testcases_brute_force:
        days, expected = test
        assert lanternfish_brute_force(fish, days) == expected


def test_lanternfish_perf():

    testcases = testcases_brute_force + [(NR_OF_DAYS_PART_2, 26984457539)]

    for test in testcases:
        days, expected = test
        assert lanternfish_perf(fish, days) == expected
