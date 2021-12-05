from types import Tuple


def part_one(bingo_input: list[str]) -> int:
    pass


def part_two(bingo_input: list[str]) -> int:
    pass


def parse_bingo_input(bingo_input: list[str]) -> Tuple[list[int], list[list[int]]]:
    drawn_numbers = [int(num) for num in bingo_input[0]]
    bingo_boards = [[int(num) for num in row.split()] for row in bingo_input[1:]]
    return (drawn_numbers, bingo_boards)
