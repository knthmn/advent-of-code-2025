def parse(line: str):
    intervals = line.split(",")
    for interval in intervals:
        a, b = interval.split("-")
        yield int(a), int(b)


def part_1(line: str):
    intervals = list(parse(line))
    max_number = max(interval[1] for interval in intervals)
    i = 1
    s = 0
    while True:
        repeated_number = int(str(i) * 2)
        if repeated_number > max_number:
            break
        if any(interval[0] <= repeated_number <= interval[1] for interval in intervals):
            s += repeated_number
        i += 1
    return s


def part_2(line: str):
    intervals = list(parse(line))
    max_number = max(interval[1] for interval in intervals)
    i = 1
    invalid_numbers = set()
    while True:
        for j in range(2, 10):
            repeated_number = int(str(i) * j)
            if j == 2 and repeated_number > max_number:
                return sum(invalid_numbers)
            if repeated_number > max_number:
                break
            if any(
                interval[0] <= repeated_number <= interval[1] for interval in intervals
            ):
                invalid_numbers.add(repeated_number)
        i += 1


def test_part_1():
    with open("d02/example1.txt") as f:
        assert part_1(f.readlines()[0]) == 1227775554


def test_part_2():
    with open("d02/example1.txt") as f:
        assert part_2(f.readlines()[0]) == 4174379265


def main():
    with open("d02/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines[0]))
    print(part_2(lines[0]))


if __name__ == "__main__":
    main()
