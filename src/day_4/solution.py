from collections import defaultdict
import os
import re

from pydantic import BaseModel, computed_field

class Card(BaseModel):
    card_number: int
    winning_numbers: set[int]
    numbers: set[int]

    @computed_field
    @property
    def winners(self) -> set[int]:
        return self.winning_numbers.intersection(self.numbers)


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]):
    cards = []
    for line in lines:
        match = re.match(r"Card\s+(\d+): ([^|]+?) \| ([^|]+?)$", line)

        if not match:
            raise Exception(f"Invalid line: {line}")

        cards.append(
            Card(
                card_number=int(match.group(1)),
                winning_numbers=set(int(x) for x in match.group(2).split()),
                numbers=set(int(x) for x in match.group(3).split()),
            )
        )

    return cards


def sum_winning_points(cards: list[Card]) -> int:
    points = 0
    for card in cards:
        winners = card.winners
        if winners:
            # One winner gets 1 point, every other winner doubles the points
            points += 1 << (len(winners) - 1)

    return points


def process_cards(cards: list[Card]) -> dict[int, int]:
    """ Returns a dictionary with the count of each card number """
    counts = defaultdict(int)
    for card in cards:
        counts[card.card_number] += 1
        multiplier = counts[card.card_number]
        for winner in range(len(card.winners)):
            card_number = card.card_number + winner + 1
            counts[card_number] = counts[card_number] + multiplier

    return counts


def solution_a() -> int:
    cards = parse_input(get_input())
    return sum_winning_points(cards)


def solution_b() -> int:
    cards = parse_input(get_input())
    counts = process_cards(cards)
    return sum(counts.values())
