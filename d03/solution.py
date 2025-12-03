def solve(lines: list[str], length: int):
    s = 0
    for line in lines:
        numbers = [int(c) for c in line.strip()]
        chosen_numbers = []
        start_idx = 0
        while len(chosen_numbers) < length:
            numbers_to_choose = length - len(chosen_numbers)
            idx_largest = start_idx
            largest = numbers[start_idx]
            for idx, number in enumerate(
                numbers[start_idx : -numbers_to_choose + 1 + len(numbers)]
            ):
                if number > largest:
                    largest = number
                    idx_largest = idx + start_idx
            chosen_numbers.append(largest)
            start_idx = idx_largest + 1
        s += sum(
            number * 10**pow for pow, number in enumerate(reversed(chosen_numbers))
        )
    return s


def part_1(lines: list[str]):
    return solve(lines, 2)


def part_2(lines: list[str]):
    return solve(lines, 12)


def test_part_1():
    with open("d03/example1.txt") as f:
        assert part_1(f.readlines()) == 357


def test_part_2():
    with open("d03/example1.txt") as f:
        assert part_2(f.readlines()) == 3121910778619


def main():
    with open("d03/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
