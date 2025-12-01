import re


def parse(lines: list[str]):
    for line in lines:
        direction, num = re.match(r"([LR])(\d+)", line).groups()
        num = int(num)
        if direction == "L":
            num *= -1
        yield num


def part_1(lines: list[str]):
    dial = 50
    at_zero_count = 0
    for step in parse(lines):
        dial = (dial + step) % 100
        if dial == 0:
            at_zero_count += 1
    return at_zero_count


def part_2(lines: list[str]):
    dial = 50
    hit_zero_count = 0
    for step in parse(lines):
        if step == 0:
            continue
        new_dial = dial + step
        hit_num_min = new_dial if new_dial < dial else dial
        hit_num_max = new_dial if new_dial > dial else dial
        hit_zero_count += hit_num_max // 100 - hit_num_min // 100
        if new_dial < dial:  # two cases that need adjustment
            if new_dial % 100 == 0:
                hit_zero_count += 1
            if dial % 100 == 0:
                hit_zero_count -= 1
        dial = new_dial % 100

    return hit_zero_count


def test_part_1():
    with open("d01/example1.txt") as f:
        assert part_1(f.readlines()) == 3


def test_part_2():
    with open("d01/example1.txt") as f:
        assert part_2(f.readlines()) == 6


def main():
    with open("d01/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
