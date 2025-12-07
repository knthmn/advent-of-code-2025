def part_1(lines: list[str]):
    starting_location = lines[0].index("S")
    heads = {starting_location}

    num_splits = 0
    for y in range(1, len(lines)):
        new_heads = set()
        for x in heads:
            if lines[y][x] == "^":
                num_splits += 1
                new_heads.add(x - 1)
                new_heads.add(x + 1)
            else:
                new_heads.add(x)
        heads = new_heads
    return num_splits


def part_2(lines: list[str]):
    starting_location = lines[0].index("S")
    heads = {starting_location: 1}

    for y in range(1, len(lines)):
        new_heads = {}
        for x, n in heads.items():
            if lines[y][x] == "^":
                new_heads[x - 1] = new_heads.get(x - 1, 0) + n
                new_heads[x + 1] = new_heads.get(x + 1, 0) + n
            else:
                new_heads[x] = new_heads.get(x, 0) + n
        heads = new_heads
    return sum(heads.values())


def test_part_1():
    with open("d07/example1.txt") as f:
        assert part_1(f.readlines()) == 21


def test_part_2():
    with open("d07/example1.txt") as f:
        assert part_2(f.readlines()) == 40


def main():
    with open("d07/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
