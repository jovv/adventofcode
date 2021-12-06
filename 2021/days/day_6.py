from collections import Counter
from typing import Dict, List

from days.inputreader import day_input, day

NR_OF_DAYS_PART_1 = 80
NR_OF_DAYS_PART_2 = 256


def initial_state(s: str) -> List[int]:
    return [int(x) for x in s[0].strip().split(',')]


def lanternfish_brute_force(state: List[int], days: int) -> int:

    for _ in range(days):

        zeros = Counter(state)[0]
        state = [6 if n == 0 else n - 1 for n in state]

        state += [8] * zeros

    return len(state)


def fish_state_count(cnts) -> Dict[int, int]:
    return {i: cnts.get(i, 0) for i in range(8 + 1)}


def lanternfish_perf(state: List[int], days: int) -> int:

    cntr = fish_state_count(Counter(state))
    for d in range(days):
        tmp_cntr = cntr.copy()
        for k in cntr.keys():
            if k == 6:
                tmp_cntr[6] = cntr[7] + cntr[0]
            elif k == 8:
                tmp_cntr[8] = cntr[0]
            else:
                tmp_cntr[k] = cntr[k + 1]

        cntr = tmp_cntr.copy()

    return sum(cntr.values())


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    state: List[int] = initial_state(content)

    part1 = lanternfish_brute_force(state, NR_OF_DAYS_PART_1)
    part2 = lanternfish_perf(state, NR_OF_DAYS_PART_2)

    print(part1)
    print(part2)
