from day_10 import solution


def test_parse_input():
    lines = [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        "....."
    ]

    assert solution.parse_input(lines) == solution.Field(
        start=solution.Point(x=1, y=1),
        layout=[
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
        ]
    )


def test_get_neighbors():
    lines = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]

    field = solution.parse_input(lines)
    assert solution.get_neighbors(field.start, field) == {
        solution.Point(x=1, y=2),
        solution.Point(x=2, y=1),
    }


def test_find_cycle():
    lines = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]

    field = solution.parse_input(lines)
    solution.find_cycle(field)
    assert max(field.cycle.values()) == 4

    lines = [
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ]

    field = solution.parse_input(lines)
    solution.find_cycle(field)
    assert max(field.cycle.values()) == 8


def test_get_inner_tiles():
    lines = [
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||....||.",
        ".||....||.",
        ".|L-7F-J|.",
        ".|..||..|.",
        ".L--JL--J.",
        "..........",
    ]

    field = solution.parse_input(lines)
    assert len(solution.get_inner_tiles(field)) == 4

