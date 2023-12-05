import os
import re

from pydantic import BaseModel

class AlmanacMap():
    def __init__(self):
        self.source_start: list[int] = list()
        self.destination_start: list[int] = list()
        self.range: list[int] = list()

    def add_mapping(self, source_start: int, destination_start: int, range: int):
        self.source_start.append(source_start)
        self.destination_start.append(destination_start)
        self.range.append(range)

    def __getitem__(self, source: int) -> int:
        for i in range(len(self.source_start)):
            if source >= self.source_start[i] and source < self.source_start[i] + self.range[i]:
                return self.destination_start[i] + (source - self.source_start[i])
        return source


class MappingData(BaseModel):
    source: int
    destination: int
    range: int

    def __str__(self):
        return f"{self.source}:{self.source + self.range} - {self.destination}:{self.destination + self.range}"

class Almanac():
    def __init__(self, seeds: list[int] | None):
        if seeds is None:
            seeds = list()
        self.seeds: list[int] = seeds
        self.seed_to_soil: AlmanacMap = AlmanacMap()
        self.soil_to_fertilizer: AlmanacMap = AlmanacMap()
        self.fertilizer_to_water: AlmanacMap = AlmanacMap()
        self.water_to_light: AlmanacMap = AlmanacMap()
        self.light_to_temperature: AlmanacMap = AlmanacMap()
        self.temperature_to_humidity: AlmanacMap = AlmanacMap()
        self.humidity_to_location: AlmanacMap = AlmanacMap()


    def seed_locations(self) -> list[int]:
        locations = []
        for seed in self.seeds:
            step_value = seed
            for map in (
                    "seed_to_soil",
                    "soil_to_fertilizer",
                    "fertilizer_to_water",
                    "water_to_light",
                    "light_to_temperature",
                    "temperature_to_humidity",
                    "humidity_to_location",
            ):
                step_value = getattr(self, map)[step_value]

            locations.append(step_value)
        return locations

    def seed_range_location(self) -> int:
        min_location = None
        i = 0
        while i < len(self.seeds):
            start = self.seeds[i]
            seed_range = self.seeds[i + 1]
            print(f"#\n# start: {start}, seed_range: {seed_range} ({i + 1} / {int(len(self.seeds) / 2)})\n#")
            i += 2

            for seed in range(start, start + seed_range):
                if seed % 1000000 == 0:
                    print(f"\t{seed}: {int((seed - start) / seed_range * 100)}%")
                step_value = seed
                for map in (
                        "seed_to_soil",
                        "soil_to_fertilizer",
                        "fertilizer_to_water",
                        "water_to_light",
                        "light_to_temperature",
                        "temperature_to_humidity",
                        "humidity_to_location",
                ):
                    step_value = getattr(self, map)[step_value]
                if step_value == 1:
                    print("One")
                if min_location is None or step_value < min_location:
                    min_location = step_value

        return min_location


def get_input() -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "input.txt")) as infile:
        return [x.strip() for x in infile.readlines()]


def parse_input(lines: list[str]) -> Almanac:
    # Seeds
    if match := re.match(r"seeds: (.+)$", lines[0]):
        almanac = Almanac(seeds=[int(x) for x in match.group(1).split(" ")])
    else:
        raise Exception("Invalid input")

    line_number = 1
    map_category = None

    while line_number < len(lines):
        line = lines[line_number]

        if line == "":
            line_number += 1
            continue

        # Headers
        if (match := re.match(r"([a-z-]+) map:", line)):
            map_category = match.group(1)
            map_category = map_category.replace("-", "_")
            line_number += 1
            continue

        # Maps
        if not line[0].isdigit():
            raise Exception(f"Expected digit, #{line_number}: {line}")

        digits = [int(x) for x in line.split(" ")]
        if len(digits) != 3:
            raise Exception(f"Expected three integers, #{line_number}: {line}")

        if not map_category:
            raise Exception(f"Expected map category to have been set, #{line_number}: {line}")

        getattr(almanac, map_category).add_mapping(digits[1], digits[0], digits[2])

        line_number += 1

    return almanac


def solution_a() -> int:
    lines = get_input()
    almanac = parse_input(lines)
    return min(almanac.seed_locations())


def solution_b() -> int:
    lines = get_input()
    almanac = parse_input(lines)
    return almanac.seed_range_location()




