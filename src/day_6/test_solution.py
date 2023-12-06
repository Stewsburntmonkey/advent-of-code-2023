from math import prod

from day_6 import solution

LINES = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_winning_strategies():
    setup = solution.parse_input(LINES)
    strategies = solution.get_winning_strategies(setup)

    assert len(strategies) == 3
    assert prod(strategies) == 288


def test_binary_search():
    setup = solution.parse_input_fix_kerning(LINES)
    strategies = solution.get_winning_strategies(setup, solution.binary_search_strategy)

    assert len(strategies) == 1
    assert strategies[0] == 71503