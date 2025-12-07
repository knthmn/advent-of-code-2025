def parse(lines: list[str]):
    lines = [line.strip() for line in lines]
    blank_line_idx = lines.index("")
    fresh_ingredient_ranges = [
        (int(line.split("-")[0]), int(line.split("-")[1]))
        for line in lines[:blank_line_idx]
    ]
    available_ingredients = [int(line) for line in lines[blank_line_idx + 1 :]]
    return fresh_ingredient_ranges, available_ingredients


def part_1(lines: list[str]):
    fresh_ingredient_ranges, available_ingredients = parse(lines)
    s = 0
    for ingredient in available_ingredients:
        for range_start, range_end in fresh_ingredient_ranges:
            if range_start <= ingredient <= range_end:
                s += 1
                break
    return s


def part_2(lines: list[str]):
    fresh_ingredient_ranges, _ = parse(lines)
    fresh_ingredient_ranges.sort(key=lambda r: r[0])

    sanitized_ranges = []
    for r in fresh_ingredient_ranges:
        start, end = r
        if len(sanitized_ranges) >= 1 and start <= sanitized_ranges[-1][1]:
            start = min(start, sanitized_ranges[-1][0])
            end = max(end, sanitized_ranges[-1][1])
            sanitized_ranges.pop()
        sanitized_ranges.append((start, end))

    return sum(r[1] - r[0] + 1 for r in sanitized_ranges)


def test_part_1():
    with open("d05/example1.txt") as f:
        assert part_1(f.readlines()) == 3


def test_part_2():
    with open("d05/example1.txt") as f:
        assert part_2(f.readlines()) == 14


def main():
    with open("d05/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
