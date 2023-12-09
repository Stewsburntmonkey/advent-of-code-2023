import os

import numpy


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> list[list[int]]:
    dataset = []
    for line in lines:
        dataset.append([int(x) for x in line.split()])

    return dataset


def next_number(numbers: list[int]) -> int:
    next_num = 0
    working = numpy.array(numbers)
    while numpy.count_nonzero(working) > 1:
        next_num += working[-1]
        working = numpy.diff(working)

    return next_num


def previous_number(numbers: list[int]) -> int:
    left_most = []
    working = numpy.array(numbers)
    while numpy.count_nonzero(working) > 1:
        left_most.append(working[0])
        working = numpy.diff(working)

    previous_num = 0
    for x in reversed(left_most):
        previous_num = x - previous_num

    return previous_num


def solution_a() -> int:
    dataset = parse_input(get_input())
    return sum([next_number(x) for x in dataset])


def solution_b() -> int:
    dataset = parse_input(get_input())
    return sum([previous_number(x) for x in dataset])
