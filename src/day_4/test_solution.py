from day_4 import solution

LINES = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

def test_parse_input():
    cards = solution.parse_input(LINES)
    assert len(cards) == 6
    assert cards[0].card_number == 1
    assert cards[0].winning_numbers == {41, 48, 83, 86, 17}
    assert cards[0].numbers == {83, 86, 6, 31, 17, 9, 48, 53}


def test_winning_points():
    cards = solution.parse_input(LINES)
    assert solution.sum_winning_points(cards) == 13


def test_process_cards():
    counts = solution.process_cards(solution.parse_input(LINES))
    assert counts[1] == 1
    assert counts[5] == 14
    assert sum(counts.values()) == 30