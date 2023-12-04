import os
import re


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def get_char(lines: list[str], x: int, y: int) -> str:
    if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
        return ""

    return lines[y][x]

def get_number(lines: list[str], x: int, y: int) -> tuple[int, int | None]:
    """ Returns the number starting at the given x, y position, and the x position following the number. """
    number = ""
    adjacent = ""
    line = lines[y]
    while x < len(line):
        char = line[x]
        if char.isdigit():
            number += char
            adjacent += ''.join([
                get_char(lines, x - 1, y - 1),
                get_char(lines, x, y - 1),
                get_char(lines, x + 1, y - 1),
                get_char(lines, x - 1, y),
                get_char(lines, x + 1, y),
                get_char(lines, x - 1, y + 1),
                get_char(lines, x, y + 1),
                get_char(lines, x + 1, y + 1),
            ])

            x += 1
        else:
            break

    if re.search(r"[^\d.]", adjacent):
        number = int(number)
    else:
        number = None

    return x, number


def part_numbers(lines: list[str]) -> list[int]:
    parts = []

    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            char = line[x]
            if char.isdigit():
                next_x, number = get_number(lines, x, y)
                x = next_x
                if number is not None:
                    parts.append(int(number))
            else:
                x += 1

    return parts


def get_number_containing(lines: list[str], x: int, y: int) -> tuple[int, str]:
    """ Returns the number that includes the given x,y position and the x position of the start of the number. """
    line = lines[y]
    start_x = x
    while x >= 0:
        char = line[x]
        if char.isdigit():
            start_x = x
            x -= 1
        else:
            break

    x = start_x
    start = f"{x},{y}"

    number = ""
    while x < len(line):
        char = line[x]
        if char.isdigit():
            number += char
            x += 1
        else:
            break

    return int(number), start


def gear_ratios(lines: list[str]) -> list[int]:
    ratios = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                numbers = {}
                for x1 in [x-1, x, x+1]:
                    for y1 in [y-1, y, y+1]:
                        char = get_char(lines, x1, y1)
                        if char.isdigit():
                            number, start = get_number_containing(lines, x1, y1)
                            numbers[start] = number

                if len(numbers) == 2:
                    ratio = 1
                    for number in numbers.values():
                        ratio *= number
                    ratios.append(ratio)

    return ratios


def solution_a() -> int:
    lines = get_input()
    parts = part_numbers(lines)
    return sum(parts)


def solution_b() -> int:
    lines = get_input()
    ratios = gear_ratios(lines)
    return sum(ratios)
