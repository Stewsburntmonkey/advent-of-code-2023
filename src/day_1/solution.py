import os
import re


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_lines(lines: list[str]) -> list[str]:
    digit_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    words = "|".join(digit_map.keys())

    for line in lines:
        yield re.sub(fr"(?=({words}))", lambda x: digit_map[x.group(1)], line)


def calibration_values(lines: list[str]) -> int:
    total = 0
    for line in lines:
        first = None
        last = None
        for char in line:
            if char.isdigit():
                if first is None:
                    first = char
                last = char

        if first is None or last is None:
            raise Exception("No digits found in line")

        total += int(first + last)

    return total


def solution_a():
    lines = get_input()
    return calibration_values(lines)


def solution_b():
    lines = get_input()
    return calibration_values(list(parse_lines(lines)))
