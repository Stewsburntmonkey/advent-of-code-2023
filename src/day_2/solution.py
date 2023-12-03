import os
import re

from pydantic import BaseModel

class Blocks(BaseModel):
    number: int
    color: str

class Draw(BaseModel):
    blocks: list[Blocks] = []

class Game(BaseModel):
    game_number: int
    draws: list[Draw] = []

def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_lines(lines: list[str]) -> list[Game]:
    games = []
    for line in lines:
        match = re.match(r"Game (\d+): (.*)", line)
        if match is None:
            raise Exception("Invalid line")

        game = Game(game_number=int(match.group(1)))

        draws = match.group(2).split("; ")
        for draw in draws:
            draw_matches = re.findall(r"(\d+) (\w+)", draw)
            if draw_matches is None:
                raise Exception("Invalid draw")

            draw_obj = Draw()
            for draw_match in draw_matches:
                draw_obj.blocks.append(Blocks(number=int(draw_match[0]), color=draw_match[1]))

            game.draws.append(draw_obj)

        games.append(game)

    return games


def valid_games(maximums: dict[str, int], games: list[Game]) -> list[Game]:
    game_sum = 0

    for game in games:
        valid = True
        for draw in game.draws:
            for block in draw.blocks:
                if block.number > maximums[block.color]:
                    valid = False

        if valid:
            yield game


def valid_games_sum(games: list[Game], maximums: dict[str, int]) -> int:
    game_sum = 0
    for game in valid_games(maximums, games):
        game_sum += game.game_number

    return game_sum


def minimum_game_power(games: list[Game]) -> int:
    game_power = 0
    for game in games:
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for draw in game.draws:
            for block in draw.blocks:
                if minimums[block.color] < block.number:
                    minimums[block.color] = block.number

        game_power += minimums["red"] * minimums["green"] * minimums["blue"]

    return game_power


def solution_a():
    lines = get_input()
    games = parse_lines(lines)

    maximums = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    return valid_games_sum(games, maximums)

def solution_b():
    lines = get_input()
    games = parse_lines(lines)

    return minimum_game_power(games)




