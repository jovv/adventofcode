from days.inputreader import day_input, day
from typing import List


def nr_of_increases(xs: List[int]) -> int:
    increases = 0
    for i, v in enumerate(xs):
        if i == 0:
            continue
        if v > xs[i - 1]:
            increases += 1

    return increases


def nr_of_sliding_window_increases(xs: List[int], size: int) -> int:

    cnt = 0
    for i, _ in enumerate(xs):
        if i + 2 + 1 > size:
            break
        a = xs[i:i + 3]
        b = xs[i + 1:i + 1 + 3]
        if sum(b) > sum(a):
            cnt += 1

    return cnt


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    xs = [int(x) for x in content]

    part1 = nr_of_increases(xs)
    part2 = nr_of_sliding_window_increases(xs, len(xs))

    print(part1)
    print(part2)
