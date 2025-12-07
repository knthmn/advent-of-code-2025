from functools import reduce


def part_1(lines: list[str]):
    problems = [[s for s in line.split()] for line in lines]
    problems = [i for i in zip(*problems)]

    total = 0
    for problem in problems:
        numbers = [int(s) for s in problem[:-1]]
        if problem[-1] == "+":
            total += sum(numbers)
        else:
            total += reduce(lambda x, y: x * y, numbers)
    return total


def part_2(lines: list[str]):
    lines = [line.rstrip() for line in lines]
    max_line_length = max(len(line) for line in lines)
    lines = [line.ljust(max_line_length, " ") for line in lines]
    operator_idxs = [i for i, c in enumerate(lines[-1]) if c in ["+", "*"]]
    problem_idxs = list(zip(operator_idxs, operator_idxs[1:] + [len(lines[-1]) + 2]))

    total = 0
    for start, end in problem_idxs:
        numbers = [line[start : end - 1] for line in lines[:-1]]
        numbers = [i for i in zip(*numbers)]
        numbers = [int("".join(number).strip()) for number in numbers]
        if lines[-1][start] == "+":
            total += sum(numbers)
        else:
            total += reduce(lambda x, y: x * y, numbers)
    return total


def test_part_1():
    with open("d06/example1.txt") as f:
        assert part_1(f.readlines()) == 4277556


def test_part_2():
    with open("d06/example1.txt") as f:
        assert part_2(f.readlines()) == 3263827


def main():
    with open("d06/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
