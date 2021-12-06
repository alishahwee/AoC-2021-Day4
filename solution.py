def part_one(bingo_input: list[str]) -> int:
    numbers_to_draw, bingo_boards = parse_bingo_input(bingo_input)
    board_size = len(bingo_boards[0])

    # Initialize to first 4 numbers since no winners are possible until at least 5 draws
    numbers_drawn = numbers_to_draw[: board_size - 1]
    winning_board = None

    for num in numbers_to_draw:
        if winning_board is not None:
            break
        numbers_drawn.append(num)
        for board in bingo_boards:
            if winning_board is not None:
                break
            for row in board:
                if set(row).issubset(set(numbers_drawn)):
                    winning_board = board
                    break
            for i in range(board_size):
                #  Determines column numbers and compares it
                if set([row[i] for row in board]).issubset(set(numbers_drawn)):
                    winning_board = board
                    break

    winning_num = numbers_drawn[-1]
    unmarked_sum = 0

    for row in winning_board:
        for num in row:
            if num not in numbers_drawn:
                unmarked_sum += num

    return winning_num * unmarked_sum


def part_two(bingo_input: list[str]) -> int:
    numbers_to_draw, bingo_boards = parse_bingo_input(bingo_input)
    board_size = len(bingo_boards[0])

    # Initialize to first 4 numbers since no winners are possible until at least 5 draws
    numbers_drawn = numbers_to_draw[: board_size - 1]
    winning_boards = list()

    for num in numbers_to_draw:
        if len(winning_boards) == len(bingo_boards):
            break
        numbers_drawn.append(num)
        for board in bingo_boards:
            if len(winning_boards) == len(bingo_boards):
                break
            for row in board:
                if (
                    set(row).issubset(set(numbers_drawn))
                    and board not in winning_boards
                ):
                    winning_boards.append(board)
            for i in range(board_size):
                #  Determines column numbers and compares it
                if (
                    set([row[i] for row in board]).issubset(set(numbers_drawn))
                    and board not in winning_boards
                ):
                    winning_boards.append(board)

    winning_num = numbers_drawn[-1]
    unmarked_sum = 0

    for row in winning_boards[-1]:
        for num in row:
            if num not in numbers_drawn:
                unmarked_sum += num

    return winning_num * unmarked_sum


def parse_bingo_input(
    bingo_input: list[str],
) -> tuple[list[int], list[list[list[int]]]]:
    numbers_to_draw = [int(num) for num in bingo_input[0].split(",")]
    bingo_boards = [
        [[int(num) for num in row.split()] for row in board.split("\n")]
        for board in bingo_input[1:]
    ]
    return (numbers_to_draw, bingo_boards)
