from day_13 import solution


LINES = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


def test_summary():
    setup = solution.parse_input(LINES)
    assert solution.summary(setup) == 405

    assert solution.summary(setup, True) == 400


def test_is_reflection():
    setup = solution.parse_input(LINES)

    assert solution.is_reflection(3, setup.patterns[1]) is True
    assert solution.is_reflection(2, setup.patterns[1]) is False


def test_vertical_reflection():
    setup = solution.parse_input(LINES)

    assert solution.vertical_reflection(setup.patterns[0]) == 5
    assert solution.vertical_reflection(setup.patterns[1]) == 0


def test_horizontal_reflection():
    setup = solution.parse_input(LINES)

    assert solution.horizontal_reflection(setup.patterns[0]) == 0
    assert solution.horizontal_reflection(setup.patterns[1]) == 4
