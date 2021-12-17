from collections import Counter
from typing import List, Tuple

from days.inputreader import day_input, day

OXYGEN = 'O2'
CO2 = 'CO2'


def transpose(m: List[str]) -> List[str]:
    return [''.join(list(tup)) for tup in zip(*[list(li) for li in m])]


def most_common(line: str) -> Tuple[str, str]:
    cntr: List[Tuple[str, int]] = Counter(line).most_common()
    if cntr[0][1] != cntr[1][1]:
        return cntr[0][0], cntr[1][0]
    else:
        return '1', '0'


def power_consumption(lines: List[str]) -> int:
    gamma_rate = ''
    epsilon_rate = ''
    base = 2

    for line in transpose(lines):
        cntr: List[Tuple[str, int]] = Counter(line).most_common()
        gamma_rate += cntr[0][0]
        epsilon_rate += cntr[1][0]

    return int(gamma_rate, base) * int(epsilon_rate, base)


def rating(xs: List[str], idx: int, typ: str) -> int:
    if len(xs) != 1:
        xs_t = transpose(xs)
        most, least = most_common(xs_t[idx])
        keep = most if typ == OXYGEN else least
        return rating([nr for nr in xs if nr[idx] == keep], idx + 1, typ)
    else:
        return xs[0]


def life_support_rating(lines: List[str]) -> int:
    base = 2

    oxygen = rating(lines, 0, OXYGEN)
    co2 = rating(lines, 0, CO2)

    return int(oxygen, base) * int(co2, base)


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    lines = [line.strip() for line in content]
    part1 = power_consumption(lines)
    part2 = life_support_rating(lines)

    print(part1)
    print(part2)
