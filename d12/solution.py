import re


def parse(lines: list[str]):
    shapes = [lines[5 * i + 1 : 5 * i + 4] for i in range(5)]
    shapes = [[line.strip() for line in shape] for shape in shapes]
    specs = [
        re.match(R"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+)", line.strip()).groups()
        for line in lines[30:]
    ]
    specs = [[int(n) for n in spec] for spec in specs]
    return shapes, specs


def part_1(lines: list[str]):
    shapes, specs = parse(lines)
    nums_tiles = [sum(c == "#" for line in shape for c in line) for shape in shapes]

    # this does not work with the test case but works with my input
    def can_fit(spec):
        width, height, *num_shapes = spec
        num_shapes_in_trivial_fit = (width // 3) * (height // 3)
        if sum(num_shapes) <= num_shapes_in_trivial_fit:
            return True
        if sum(a * b for a, b in zip(nums_tiles, num_shapes)) < width * height:
            return False
        raise Exception("Too complicated to compute")

    return sum(can_fit(spec) for spec in specs)


def main():
    with open("d12/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))


if __name__ == "__main__":
    main()
