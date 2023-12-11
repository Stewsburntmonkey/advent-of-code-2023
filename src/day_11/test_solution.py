from day_11 import solution

import numpy as np

from pprint import pprint


LINES = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


def test_parse_input():
    actual = solution.parse_input(LINES)
    expected = np.array(
        [
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        ]
    )

    assert np.array_equal(actual, expected)


def test_expand_universe():
    sky_map = solution.parse_input(LINES)
    actual = solution.expand_universe(sky_map)
    expected = np.array(
        [
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
            [1, 1, 2, 1, 1, 2, 1, 1, 2, 1]
        ]
    )

    assert np.array_equal(actual, expected)


def test_sum_shortest_paths():
    sky_map = solution.SkyMap(solution.parse_input(LINES), 2)
    actual = solution.sum_shortest_paths(sky_map)

    assert actual == 374
