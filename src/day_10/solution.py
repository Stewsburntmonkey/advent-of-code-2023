import os

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


class Field(BaseModel):
    start: Point
    layout: list[list[str]]
    cycle: dict[Point, int] | None = None


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(input: list[str]) -> Field:
    start = None
    layout = []
    for y, line in enumerate(input):
        layout.append([])
        for x, char in enumerate(line):
            layout[y].append(char)

            if char == "S":
                start = Point(x=x, y=y)

    return Field(start=start, layout=layout)


def get_neighbors(point: Point, field: Field) -> set[Point]:
    char = field.layout[point.y][point.x]

    match char:
        case ".":
            return set()
        case "|":
            return {
                Point(x=point.x, y=point.y - 1),
                Point(x=point.x, y=point.y + 1)
            }
        case "-":
            return {
                Point(x=point.x - 1, y=point.y),
                Point(x=point.x + 1, y=point.y)
            }
        case "F":
            return {
                Point(x=point.x, y=point.y + 1),
                Point(x=point.x + 1, y=point.y)
            }
        case "L":
            return {
                Point(x=point.x, y=point.y - 1),
                Point(x=point.x + 1, y=point.y)
            }
        case "J":
            return {
                Point(x=point.x, y=point.y - 1),
                Point(x=point.x - 1, y=point.y)
            }
        case "7":
            return {
                Point(x=point.x, y=point.y + 1),
                Point(x=point.x - 1, y=point.y)
            }
        case "S":
            neighbors = set()
            for x,y in [(point.x, point.y - 1), (point.x, point.y + 1), (point.x - 1, point.y), (point.x + 1, point.y)]:
                if not 0 <= x < len(field.layout[0]):
                    continue
                if not 0 <= y < len(field.layout):
                    continue

                neighbor = Point(x=x, y=y)
                neighbor_neighbors = get_neighbors(neighbor, field)
                if point in neighbor_neighbors:
                    neighbors.add(neighbor)

            for possible_char in ["F", "L", "J", "7", "|", "-"]:
                field.layout[point.y][point.x] = possible_char
                if get_neighbors(point, field) == neighbors:
                    return neighbors

    raise ValueError(f"Unknown character: {char}")


def find_cycle(field: Field):
    field.cycle = {field.start: 0}

    queue = [field.start]
    while queue:
        current = queue.pop(0)
        current_distance = field.cycle[current]

        for neighbor in get_neighbors(current, field):
            if neighbor not in field.cycle or field.cycle[neighbor] > current_distance + 1:
                field.cycle[neighbor] = current_distance + 1
                queue.append(neighbor)


def get_inner_tiles(field: Field) -> set[Point]:
    find_cycle(field)

    inner_tiles = set()

    for y, row in enumerate(field.layout):
        pending = ""
        is_inner = False
        for x, char in enumerate(row):
            point = Point(x=x, y=y)
            if point not in field.cycle:
                if is_inner:
                    inner_tiles.add(point)
                continue

            match char:
                case "|":
                    is_inner = not is_inner
                case "F":
                    if pending != "":
                        raise ValueError(f"Invalid layout: {x}, {y} [{pending}]")
                    pending = "F"
                    continue
                case "L":
                    if pending != "":
                        raise ValueError(f"Invalid layout: {x}, {y} [{pending}]")
                    pending = "L"
                    continue
                case "7":
                    if pending not in {"F", "L"}:
                        raise ValueError(f"Invalid layout: {x}, {y} [{pending}]")
                    if pending == "L":
                        is_inner = not is_inner

                    pending = ""
                    continue
                case "J":
                    if pending not in {"F", "L"}:
                        raise ValueError(f"Invalid layout: {x}, {y} [{pending}]")
                    if pending == "F":
                        is_inner = not is_inner

                    pending = ""
                    continue
                case "-":
                    continue
                case _:
                    raise ValueError(f"Invalid character: {x}, {y} [char={char}]")

    return inner_tiles


def solution_a() -> int:
    input = get_input()
    field = parse_input(input)
    find_cycle(field)
    return max(field.cycle.values())


def solution_b() -> int:
    input = get_input()
    field = parse_input(input)
    inner_tiles = get_inner_tiles(field)
    return len(inner_tiles)
