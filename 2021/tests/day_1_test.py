from days.day_1 import nr_of_increases, nr_of_sliding_window_increases

input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_nr_of_increases():

    testcases = [(input, 7)]
    for test in testcases:
        assert nr_of_increases(test[0]) == test[1]


def test_nr_of_sliding_window_increases():
    testcases = [(input, 5)]
    for test in testcases:
        assert nr_of_sliding_window_increases(test[0], len(test[0])) == test[1]