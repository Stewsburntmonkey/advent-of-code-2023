from day_8 import solution


LINES = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

LINES_2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

GHOST_LINES = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


def test_parse_input():
    setup = solution.parse_input(LINES)

    assert setup.directions == "RL"
    assert setup.nodes["AAA"] == ("BBB", "CCC")


def test_get_path():
    setup = solution.parse_input(LINES)
    path = solution.get_path(setup)

    assert path == ["AAA", "CCC", "ZZZ"]

    setup = solution.parse_input(LINES_2)
    path = solution.get_path(setup)

    assert path == ["AAA", "BBB", "AAA", "BBB", "AAA", "BBB", "ZZZ"]


def test_ghost_path_length():
    setup = solution.parse_input(GHOST_LINES)
    path_length = solution.ghost_path_length(setup)

    assert path_length == 6
