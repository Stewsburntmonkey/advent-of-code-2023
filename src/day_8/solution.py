from math import lcm
import os

from pydantic import BaseModel


class Setup(BaseModel):
    directions: str
    nodes: dict[str, tuple[str, str]]


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> Setup:
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        node, children = line.split(" = ")
        children = tuple(children.replace("(", "").replace(")", "").split(", "))
        nodes[node] = children

    return Setup(directions=directions, nodes=nodes)


def get_path(setup: Setup) -> list[str]:
    path = []
    index = 0
    current_node = "AAA"

    while True:
        path.append(current_node)
        if current_node == "ZZZ":
            break
        if setup.directions[index] == "L":
            current_node = setup.nodes[current_node][0]
        else:
            current_node = setup.nodes[current_node][1]

        index += 1
        if index >= len(setup.directions):
            index = 0

    return path


def ghost_path_length(setup: Setup) -> int:
    index = 0
    current_nodes = [x for x in setup.nodes.keys() if x.endswith("A")]
    cycle_lengths = {}

    total = len(current_nodes)
    for i, current_node in enumerate(current_nodes):
        working_node = current_node
        print(f"{i + 1}/{total}")
        path_length = 0
        while True:
            if working_node.endswith("Z"):
                break

            path_length += 1

            direction_index = 0 if setup.directions[index] == "L" else 1
            working_node = setup.nodes[working_node][direction_index]

            index += 1
            if index >= len(setup.directions):
                index = 0

        cycle_lengths[current_node] = path_length

    return lcm(*cycle_lengths.values())


def solution_a() -> int:
    lines = get_input()
    setup = parse_input(lines)
    path = get_path(setup)

    return len(path) - 1


def solution_b() -> int:
    lines = get_input()
    setup = parse_input(lines)
    path_length = ghost_path_length(setup)

    return path_length