from math import prod
import os
import re
from typing import Callable

from pydantic import BaseModel


class Race(BaseModel):
    time: int
    distance: int


class Setup(BaseModel):
    races: list[Race] = []


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> Setup:
    if match := re.match(r"Time:\s+(.+)$", lines[0]):
        times = [int(x) for x in match.group(1).split()]
    else:
        raise Exception("Time line not found")

    if match := re.match(r"Distance:\s+(.+)$", lines[1]):
        distances = [int(x) for x in match.group(1).split()]
    else:
        raise Exception("Distance line not found")

    if len(times) != len(distances):
        raise Exception("Time and distance elements do not match")

    setup = Setup()

    for time, distance in zip(times, distances):
        setup.races.append(
            Race(
                time=time,
                distance=distance
            )
        )

    return setup


def parse_input_fix_kerning(lines: list[str]) -> Setup:
    if match := re.match(r"Time:\s+(.+)$", lines[0]):
        time = match.group(1).replace(" ", "")
    else:
        raise Exception("Time line not found")

    if match := re.match(r"Distance:\s+(.+)$", lines[1]):
        distance = match.group(1).replace(" ", "")
    else:
        raise Exception("Distance line not found")

    setup = Setup()
    setup.races.append(
        Race(
            time=int(time),
            distance=int(distance)
        )
    )

    return setup


def is_win(hold: int, time: int, distance: int) -> bool:
    return hold * (time - hold) > distance


def winning_strategies(race: Race) -> int:
    wins = 0
    for hold in range(race.time):
        if is_win(hold, race.time, race.distance):
            wins += 1

    return wins


def binary_search_strategy(race: Race) -> int:
    min_win = binary_search(race, 1, race.time - 1, is_min_win)
    max_win = binary_search(race, 1, race.time - 1, is_max_win)

    return max_win - min_win + 1


def is_min_win(hold: int, race: Race) -> int:
    if is_win(hold, race.time, race.distance):
        if not is_win(hold - 1, race.time, race.distance):
            return 0
        else:
            return -1

    return 1


def is_max_win(hold: int, race: Race) -> int:
    if is_win(hold, race.time, race.distance):
        if not is_win(hold + 1, race.time, race.distance):
            return 0
        else:
            return 1

    return -1


def binary_search(race: Race, start: int, end: int, comparator: Callable) -> int:
    middle = ((end - start) // 2) + start

    comp = comparator(middle, race)
    if comp == 0:
        return middle
    elif comp < 0:
        return binary_search(race, start, middle - 1, comparator)
    else:
        return binary_search(race, middle + 1, end, comparator)


def get_winning_strategies(setup: Setup, strategy: Callable = winning_strategies) -> list[int]:
    ways_to_win = []
    for race in setup.races:
        ways_to_win.append(strategy(race))

    return ways_to_win


def solution_a() -> int:
    lines = get_input()
    setup = parse_input(lines)
    ways_to_win = get_winning_strategies(setup)

    return prod(ways_to_win)


def solution_b() -> int:
    lines = get_input()
    setup = parse_input_fix_kerning(lines)
    ways_to_win = get_winning_strategies(setup, binary_search_strategy)

    return ways_to_win[0]