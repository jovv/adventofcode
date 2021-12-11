import numpy as np
from scipy import signal

from days.inputreader import day


def nr_of_flashes(energy_levels: np.ndarray) -> int:
    steps = 100
    nr_of_flashes = 0

    for _ in range(steps):
        energy_levels += 1
        flashed_octopi = np.zeros_like(energy_levels)

        while np.any(energy_levels, where=energy_levels > 9):
            flashing_octopi = energy_levels > 9
            all_adjacents = signal.convolve2d(
                flashing_octopi, np.ones((3, 3)), mode='same').astype(np.uint8)
            energy_levels += all_adjacents
            energy_levels[np.where(flashing_octopi)] = 0
            flashed_octopi += flashing_octopi

        nr_of_flashes += np.sum(flashed_octopi).astype(np.uint8)
        energy_levels[np.where(flashed_octopi)] = 0

    return nr_of_flashes


def steps_to_synced_flash(energy_levels: np.ndarray) -> int:

    step = 0
    flashed_octopi = np.zeros_like(energy_levels)
    while np.sum(flashed_octopi) != 100:
        step += 1
        energy_levels += 1
        flashed_octopi = np.zeros_like(energy_levels)

        while np.any(energy_levels, where=energy_levels > 9):
            flashing_octopi = energy_levels > 9
            all_adjacents = signal.convolve2d(
                flashing_octopi, np.ones((3, 3)), mode='same').astype(np.uint8)
            energy_levels += all_adjacents
            energy_levels[np.where(flashing_octopi)] = 0
            flashed_octopi += flashing_octopi

        energy_levels[np.where(flashed_octopi)] = 0

    return step


if __name__ == '__main__':

    energy_levels = np.genfromtxt(
        f'{day(__file__)}_input.txt', delimiter=1, dtype=np.uint8)

    part1 = nr_of_flashes(energy_levels)
    part2 = steps_to_synced_flash(energy_levels)

    print(part1)
    print(part2)
