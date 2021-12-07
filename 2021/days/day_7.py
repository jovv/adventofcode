from typing import List

from days.day_6 import initial_state
from days.inputreader import day_input, day

FUEL_BURN_RATE_CONSTANT = 'CONSTANT'
FUEL_BURN_RATE_INCREASING = 'INCREASING'


def fuel_burn(position: int, crab_position: int, rate: str) -> int:
    if rate == FUEL_BURN_RATE_CONSTANT:
        return abs(position - crab_position)
    elif rate == FUEL_BURN_RATE_INCREASING:
        return sum(range(abs(position - crab_position) + 1))
    else:
        raise ValueError(f'{rate} is not a valid fuel burn rate.')


def align(positions: List[int], fuel_burn_rate: str) -> int:
    max_pos = max(positions)
    total_fuel = max_pos * sum(range(len(positions) + 1))
    for i in range(1, max_pos + 1):
        fuel = 0
        for pos in positions:
            fuel += fuel_burn(pos, i, fuel_burn_rate)
        total_fuel = min(fuel, total_fuel)

    return total_fuel


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    positions: List[int] = initial_state(content)

    part1 = align(positions, FUEL_BURN_RATE_CONSTANT)
    part2 = align(positions, FUEL_BURN_RATE_INCREASING)

    print(part1)
    print(part2)
