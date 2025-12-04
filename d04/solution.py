def part_1(lines: list[str]):
    lines = [line.strip() for line in lines]
    s = 0

    def is_movable(row, col):
        num_neighboring_rolls = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (
                    0 <= r < len(lines)
                    and 0 <= c < len(lines[r])
                    and lines[r][c] == "@"
                ):
                    num_neighboring_rolls += 1
        return num_neighboring_rolls <= 4

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "@" and is_movable(row, col):
                s += 1
    return s


def part_2(lines: list[str]):
    existing_rolls = set(
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "@"
    )
    rolls_to_check = existing_rolls.copy()
    num_removed_rolls = 0

    while rolls_to_check:
        x, y = rolls_to_check.pop()
        num_neighboring_rolls = 0
        for ix in range(x - 1, x + 2):
            for iy in range(y - 1, y + 2):
                if (ix, iy) in existing_rolls and (ix, iy) != (x, y):
                    num_neighboring_rolls += 1
        if num_neighboring_rolls >= 4:
            continue
        num_removed_rolls += 1
        existing_rolls.remove((x, y))
        for ix in range(x - 1, x + 2):
            for iy in range(y - 1, y + 2):
                if (ix, iy) in existing_rolls:
                    rolls_to_check.add((ix, iy))
    return num_removed_rolls


def test_part_1():
    with open("d04/example1.txt") as f:
        assert part_1(f.readlines()) == 13


def test_part_2():
    with open("d04/example1.txt") as f:
        assert part_2(f.readlines()) == 43


def main():
    with open("d04/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
