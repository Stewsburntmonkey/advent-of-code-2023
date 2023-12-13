import os

from pydantic import BaseModel


class Setup(BaseModel):
    patterns: list[list[str]] = []


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> Setup:
    setup = Setup()
    pattern = []
    for line in lines:
        if line == "" and pattern:
            setup.patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    if pattern:
        setup.patterns.append(pattern)

    return setup


def summary(setup: Setup, smudges: bool = False, print_solutions: bool = False) -> int:
    vertical_reflections = 0
    horizontal_reflections = 0
    target_differences = 1 if smudges else 0

    for pattern in setup.patterns:
        if col := vertical_reflection(pattern, target_differences):
            vertical_reflections += col
            if print_solutions:
                print_pattern(pattern, vertical=col)
        elif row := horizontal_reflection(pattern, target_differences):
            horizontal_reflections += row
            if print_solutions:
                print_pattern(pattern, horizontal=row)
        else:
            print("0 " + ":".join(pattern))

    return vertical_reflections + (horizontal_reflections * 100)


def print_pattern(pattern: list[str], vertical: int | None = None, horizontal: int | None = None):
    if vertical is not None:
        row_nums = ""
        row_header = ""

        for i in range(len(pattern[0])):
            row_nums += str(i + 1)[-1]
            if i == vertical:
                row_header += ">"
            elif i == vertical + 1:
                row_header += "<"
            else:
                row_header += " "

        print(row_nums)
        print(row_header)
        print("\n".join(pattern))
        print(row_header)
        print(row_nums)

    elif horizontal is not None:
        for i, row in enumerate(pattern):
            row_header = " "
            line = str(i + 1)
            if i == horizontal:
                row_header = "v"
            elif i == horizontal + 1:
                row_header = "^"
            line += row_header + row + row_header + str(i + 1)
            print(line)

    else:
        print("\n".join(pattern))

    print("\n\n")


def vertical_reflection(pattern: list[str], target_differences: int = 0) -> int:
    reoriented = ["".join([x[i] for x in pattern]) for i in range(len(pattern[0]))]

    for i in range(len(reoriented) - 1):
        if is_reflection(i, reoriented, target_differences):
            return i + 1

    return 0


def horizontal_reflection(pattern: list[str], target_differences: int = 0) -> int:
    for i in range(len(pattern) - 1):
        if is_reflection(i, pattern, target_differences):
            return i + 1

    return 0


def is_reflection(i: int, pattern: list[str], target_differences: int = 0) -> bool:
    index_a = i
    index_b = i+1
    differences = 0

    while (0 <= index_a < len(pattern)) and (0 <= index_b < len(pattern)):
        differences += diff(pattern[index_a], pattern[index_b])
        if differences > target_differences:
            return False

        index_a -= 1
        index_b += 1

    if differences == target_differences:
        return True

    return False


def diff(s1: str, s2: str) -> int:
    return sum(1 for x, y in zip(s1, s2) if x != y)


def solution_a() -> int:
    lines = get_input()
    setup = parse_input(lines)
    return summary(setup)


def solution_b() -> int:
    lines = get_input()
    setup = parse_input(lines)
    return summary(setup, True)


