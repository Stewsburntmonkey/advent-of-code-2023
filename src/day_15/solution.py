import os
import re


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def hash_term(sequence: str) -> int:
    hash_value = 0
    for char in sequence:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256

    return hash_value


def hash_sum(sequence: str) -> int:
    return sum([hash_term(x) for x in sequence.split(",")])


def initialize(sequence: str) -> int:
    boxes = [{} for _ in range(256)]

    for term in sequence.split(","):
        match_data = re.match(r"(\w+)([=-])(\d+)?", term)
        label = match_data.group(1)
        operation = match_data.group(2)

        match operation:
            case "=":
                boxes[hash_term(label)][label] = int(match_data.group(3))
            case "-":
                if label in boxes[hash_term(label)]:
                    del boxes[hash_term(label)][label]

    power = 0
    for i, box in enumerate(boxes):
        for s, focal_length in enumerate(box.values()):
            power += (i + 1) * (s + 1) * focal_length

    return power


def solution_a() -> int:
    return hash_sum(get_input()[0])


def solution_b() -> int:
    return initialize(get_input()[0])
