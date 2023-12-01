from day_1 import solution


def test_calibration():
    lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    actual = solution.calibration_values(lines)

    assert actual == 142


def test_get_input():
    actual = solution.get_input()

    assert len(actual) == 1000
    assert actual[0] == "nqninenmvnpsz874"
    assert actual[-1] == "nineninekfp49"


def test_parse_lines():
    lines = [
        "one2three",
        "1four5six",
        "oneeight",
    ]

    actual = list(solution.parse_lines(lines))
    assert len(actual) == 3
    assert actual[0] == "1one23three"
    assert actual[1] == "14four56six"
    assert actual[2] == "1one8eight"


def test_parsed_calibration():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    actual = solution.calibration_values(list(solution.parse_lines(lines)))
    assert actual == 281