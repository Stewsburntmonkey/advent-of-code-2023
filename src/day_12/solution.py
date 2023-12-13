import os
from functools import cache


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def possible_arrangements(line: str, folded: bool = False) -> int:
    springs, groups = line.split()

    if folded:
        springs, groups = unfold(springs, groups)

    return arrange_springs(springs, groups)


@cache
def arrange_springs(springs: str, groups: str, in_group: bool = False) -> int:
    groups = [int(x) for x in groups.split(",")] if groups else []
    count_arrangements = 0

    if not springs:
        if not groups or groups == [0]:
            return 1
        else:
            return 0

    if not is_valid(springs, groups, in_group):
        return 0

    char = springs[0]
    if char == "?":
        if groups and groups[0]:
            count_arrangements += arrange_springs("#" + springs[1:], group_string(groups), in_group)
        count_arrangements += arrange_springs("." + springs[1:], group_string(groups), in_group)

    if groups and not groups[0]:
        groups = groups[1:]

    if char == "#":
        count_arrangements += arrange_springs(springs[1:], group_string(decrement_groups(groups)), True)
    if char == ".":
        count_arrangements += arrange_springs(springs[1:], group_string(groups), False)

    return count_arrangements


def is_valid(springs: str, groups: list[int], in_group: bool) -> bool:
    if groups and groups[0] < 0:
        return False

    if not groups or groups == [0]:
        if "#" in springs:
            return False
        else:
            return True

    if in_group:
        if groups[0] > 0:
            if springs[0] in {"?", "#"}:
                return True
            else:
                return False
        else:
            if springs[0] == "#":
                return False
            else:
                return True

    return True


def group_string(group_list: list[int]) -> str:
    return ",".join([str(x) for x in group_list])

def decrement_groups(groups: list[int]) -> list[int]:
    groups = groups.copy()
    groups[0] -= 1

    return groups


def unfold(springs: str, groups: str) -> tuple[str, str]:
    return "?".join([springs] * 5), ",".join([groups] * 5)


def solution_a() -> int:
    input = get_input()
    return sum(possible_arrangements(line) for line in input)


def solution_b() -> int:
    input = get_input()
    return sum(possible_arrangements(line, True) for line in input)
