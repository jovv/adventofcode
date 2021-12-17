from math import ceil, floor
from statistics import mean, median
from typing import List

from days.day_6 import initial_state
from days.inputreader import day_input, day

FUEL_BURN_RATE_CONSTANT = 'CONSTANT'
FUEL_BURN_RATE_INCREASING = 'INCREASING'


def fuel_burn(position: int, crab_position: int, rate: str) -> int:
    if rate == FUEL_BURN_RATE_CONSTANT:
        return abs(position - crab_position)
    else:
        return sum(range(abs(position - crab_position) + 1))


# brute force
def align(positions: List[int], fuel_burn_rate: str) -> int:
    min_pos, max_pos = min(positions), max(positions)
    total_fuel = max_pos * sum(range(len(positions) + 1))
    for i in range(min_pos, max_pos + 1):
        fuel = 0
        for pos in positions:
            fuel += fuel_burn(pos, i, fuel_burn_rate)
        total_fuel = min(fuel, total_fuel)

    return total_fuel


# need both rounding options, as the mean is a float
def means(xs: List[int]) -> List[int]:
    return [floor(mean(xs)), ceil(mean(xs))]


def align_perf(positions: List[int], fuel_burn_rate: str) -> int:

    optimals = [
        int(median(positions))
    ] if fuel_burn_rate == FUEL_BURN_RATE_CONSTANT else means(positions)

    return min([
        sum([fuel_burn(m, pos, fuel_burn_rate) for pos in positions])
        for m in optimals
    ])


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    positions: List[int] = initial_state(content)

    part1 = align_perf(positions, FUEL_BURN_RATE_CONSTANT)
    part2 = align_perf(positions, FUEL_BURN_RATE_INCREASING)

    print(part1)
    print(part2)
