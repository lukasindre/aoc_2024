import requests

import aoc_2024.util.settings


def get_input(day: int, year: int) -> str:
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"Cookie": aoc_2024.util.settings.values.AOC_SESSION},
    )
    response.raise_for_status()
    return response.text
