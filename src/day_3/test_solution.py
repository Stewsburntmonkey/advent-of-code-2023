from day_3 import solution

LINES = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

def test_get_char():
    assert solution.get_char(LINES, 0, 0) == "4"
    assert solution.get_char(LINES, 2, 0) == "7"
    assert solution.get_char(LINES, -1, 0) == ""
    assert solution.get_char(LINES, 0, -100) == ""


def test_get_number():
    assert solution.get_number(LINES, 0, 0) == (3, 467)


def test_part_numbers():
    parts = solution.part_numbers(LINES)

    assert sum(parts) == 4361


def test_gear_ratios():
    ratios = solution.gear_ratios(LINES)

    assert sum(ratios) == 467835
