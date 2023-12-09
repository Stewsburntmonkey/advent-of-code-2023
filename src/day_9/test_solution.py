from day_9 import solution


LINES = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def test_next_number():
    input = solution.parse_input(LINES)
    assert solution.next_number(input[0]) == 18
    assert solution.next_number(input[1]) == 28
    assert solution.next_number(input[2]) == 68
    assert solution.next_number([3, -2, -7, -12, -17, -22, -27, -32, -37, -42, -47, -52, -57, -62, -67, -72, -77, -82, -87, -92, -97]) == -102


def test_previous_number():
    input = solution.parse_input(LINES)
    assert solution.previous_number(input[0]) == -3
    assert solution.previous_number(input[1]) == 0
    assert solution.previous_number(input[2]) == 5
    assert solution.previous_number([10, 13, 16, 21, 30, 4]) == 5