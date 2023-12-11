import os

import numpy as np


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> np.array:
    return np.array([[1 if x == "#" else 0 for x in line] for line in lines])


class SkyMap:
    def __init__(self, sky_map: np.array, expansion_factor):
        self.galaxies = np.argwhere(sky_map == 1)
        self.distances = expand_universe(sky_map, expansion_factor)


def expand_universe(sky_map: np.array, expansion_factor: int) -> np.array:
    zero_rows = np.all(sky_map == 0, axis=1)
    zero_cols = np.all(sky_map == 0, axis=0)

    sky_map[zero_rows] = expansion_factor
    sky_map[:, zero_cols] = expansion_factor

    return np.where(sky_map == 0, 1, sky_map)


def sum_shortest_paths(sky_map: SkyMap) -> int:
    sum_of_distances = 0

    for galaxy_a in sky_map.galaxies:
        for galaxy_b in sky_map.galaxies:
            if np.array_equal(galaxy_a, galaxy_b):
                continue

            sum_of_distances += np.sum(sky_map.distances[galaxy_a[0]:galaxy_b[0], galaxy_a[1]])
            sum_of_distances += np.sum(sky_map.distances[galaxy_a[0], galaxy_a[1]:galaxy_b[1]])

    return sum_of_distances


def solution_a() -> int:
    sky_map = SkyMap(parse_input(get_input()), 2)
    return sum_shortest_paths(sky_map)


def solution_b() -> int:
    sky_map = SkyMap(parse_input(get_input()), 1_000_000)
    return sum_shortest_paths(sky_map)