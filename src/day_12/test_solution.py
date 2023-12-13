from day_12 import solution


LINES = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]


def test_possible_arrangements():
    assert solution.possible_arrangements(LINES[0]) == 1
    assert solution.possible_arrangements(LINES[1]) == 4
    assert solution.possible_arrangements(LINES[2]) == 1
    assert solution.possible_arrangements(LINES[3]) == 1
    assert solution.possible_arrangements(LINES[4]) == 4
    assert solution.possible_arrangements(LINES[5]) == 10


def test_possible_arrangements_folded():
    assert solution.possible_arrangements(LINES[0], True) == 1
    assert solution.possible_arrangements(LINES[1], True) == 16384
    assert solution.possible_arrangements(LINES[2], True) == 1
    assert solution.possible_arrangements(LINES[3], True) == 16
    assert solution.possible_arrangements(LINES[4], True) == 2500
    assert solution.possible_arrangements(LINES[5], True) == 506250
