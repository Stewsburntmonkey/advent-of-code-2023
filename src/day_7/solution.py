from collections import defaultdict, Counter
from enum import Enum
import os

from pydantic import BaseModel



sort_mapping = {
    "X": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "T": "10",
    "J": "11",
    "Q": "12",
    "K": "13",
    "A": "14",
}


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand(BaseModel):
    cards: str
    type: HandType
    sort_key: int
    bid: int


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str], jokers: bool = False) -> list[Hand]:
    hands = []

    for line in lines:
        fields = line.split()

        if len(fields) != 2:
            raise Exception(f"Invalid input: {line}")

        cards = fields[0]
        hand_type = get_hand_type_optimized(cards, jokers)
        hands.append(
            Hand(
                cards=cards,
                type=hand_type,
                sort_key=get_sort_key(cards, hand_type, jokers),
                bid=int(fields[1])
            )
        )

    return hands


def get_hand_type(cards: str, jokers: bool = False) -> HandType:
    chars = defaultdict(int)

    if jokers:
        cards = cards.replace("J", "X")

    jokers = "X" in cards

    for c in cards:
        chars[c] += 1

    by_count = defaultdict(list)
    for c, count in chars.items():
        by_count[count].append(c)

    if 5 in by_count:
        return HandType.FIVE_OF_A_KIND
    elif 4 in by_count:
        if jokers:
            return HandType.FIVE_OF_A_KIND

        return HandType.FOUR_OF_A_KIND
    elif 3 in by_count and 2 in by_count:
        if jokers:
            return HandType.FIVE_OF_A_KIND

        return HandType.FULL_HOUSE
    elif 3 in by_count:
        if jokers:
            return HandType.FOUR_OF_A_KIND

        return HandType.THREE_OF_A_KIND
    elif 2 in by_count and len(by_count[2]) == 2:
        if jokers:
            if "X" in by_count[2]:
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.FULL_HOUSE

        return HandType.TWO_PAIR
    elif 2 in by_count:
        if jokers:
            return HandType.THREE_OF_A_KIND

        return HandType.ONE_PAIR
    else:
        if jokers:
            return HandType.ONE_PAIR

        return HandType.HIGH_CARD


def get_hand_type_optimized(cards: str, jokers: bool = False) -> HandType:
    if jokers:
        cards = cards.replace("J", "X")

    counter = Counter(cards)

    joker_count = counter["X"]
    if 0 < joker_count < 5:
        del counter["X"]
        counter[counter.most_common(1)[0][0]] += joker_count

    card_counts = [count for _, count in counter.most_common()]

    match card_counts:
        case [5, *_]:
            return HandType.FIVE_OF_A_KIND
        case [4, *_]:
            return HandType.FOUR_OF_A_KIND
        case [3, 2, *_]:
            return HandType.FULL_HOUSE
        case [3, *_]:
            return HandType.THREE_OF_A_KIND
        case [2, 2, *_]:
            return HandType.TWO_PAIR
        case [2, *_]:
            return HandType.ONE_PAIR
        case _ :
            return HandType.HIGH_CARD


def get_sort_key(cards: str, hand_type: HandType, jokers: bool = False) -> int:
    if jokers:
        cards = cards.replace("J", "X")

    mapped = [sort_mapping[c] for c in cards]
    return int(str(hand_type.value) + "".join(mapped))


def get_total_winnings(hands: list[Hand]) -> int:
    total = 0

    sorted_hands = sorted(hands, key=lambda x: x.sort_key)

    for i, hand in enumerate(sorted_hands):
        total += hand.bid * (i + 1)

    return total


def solution_a() -> int:
    lines = get_input()
    hands = parse_input(lines)
    return get_total_winnings(hands)


def solution_b() -> int:
    lines = get_input()
    hands = parse_input(lines, jokers=True)
    return get_total_winnings(hands)
