from day_7 import solution


LINES = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

JOKER_LINES = [
    "AAAAA 100",  # 0
    "AAAAJ 100",  # 1
    "AAAAK 100",  # 2
    "AAAJK 100",  # 3
    "AAAKK 100",  # 4
    "AAAJJ 100",  # 5
    "JJJAA 100",  # 6
    "AAAKQ 100",  # 7
    "AAAJK 100",  # 8
    "JJJAK 100",  # 9
    "AAKKQ 100",  # 10
    "AAKKJ 100",  # 11
    "AAJJK 100",  # 12
    "AAJKQ 100",  # 13
    "JJAKQ 100",  # 14
    "AKQT9 100",  # 15
    "AKQJT 100",  # 16
    "AAKQT 100",  # 17
]



def test_parse_input():
    hands = solution.parse_input(LINES)

    assert len(hands) == 5
    assert hands[0].cards == "32T3K"
    assert hands[0].type == solution.HandType.ONE_PAIR
    assert hands[0].sort_key == 20302100313
    assert hands[1].type == solution.HandType.THREE_OF_A_KIND
    assert hands[2].type == solution.HandType.TWO_PAIR


def test_parse_input_jokers():
    hands = solution.parse_input(JOKER_LINES, jokers=True)

    assert hands[0].type == solution.HandType.FIVE_OF_A_KIND
    assert hands[1].type == solution.HandType.FIVE_OF_A_KIND
    assert hands[2].type == solution.HandType.FOUR_OF_A_KIND
    assert hands[3].type == solution.HandType.FOUR_OF_A_KIND
    assert hands[4].type == solution.HandType.FULL_HOUSE
    assert hands[5].type == solution.HandType.FIVE_OF_A_KIND
    assert hands[6].type == solution.HandType.FIVE_OF_A_KIND
    assert hands[7].type == solution.HandType.THREE_OF_A_KIND
    assert hands[8].type == solution.HandType.FOUR_OF_A_KIND
    assert hands[9].type == solution.HandType.FOUR_OF_A_KIND
    assert hands[10].type == solution.HandType.TWO_PAIR
    assert hands[11].type == solution.HandType.FULL_HOUSE
    assert hands[12].type == solution.HandType.FOUR_OF_A_KIND
    assert hands[13].type == solution.HandType.THREE_OF_A_KIND
    assert hands[14].type == solution.HandType.THREE_OF_A_KIND
    assert hands[15].type == solution.HandType.HIGH_CARD
    assert hands[16].type == solution.HandType.ONE_PAIR
    assert hands[17].type == solution.HandType.ONE_PAIR



def test_get_total_winnings():
    hands = solution.parse_input(LINES)
    total = solution.get_total_winnings(hands)

    assert total == 6440


def test_get_total_winnings_jokers():
    hands = solution.parse_input(LINES, jokers=True)
    total = solution.get_total_winnings(hands)

    assert total == 5905

