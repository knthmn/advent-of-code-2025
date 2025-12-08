import re
from functools import reduce
from itertools import combinations


def part_1(lines: list[str], num_connections: int):
    positions = [
        tuple(int(number) for number in re.match(R"(\d+),(\d+),(\d+)", line).groups())
        for line in lines
    ]
    pairs = [
        (x, y, sum((ix - iy) ** 2 for ix, iy in zip(x, y)))
        for x, y in combinations(positions, 2)
    ]
    pairs.sort(key=lambda x: x[-1])

    circuits: dict[tuple[int, int, int], set[int]] = {}
    for i_connection in range(num_connections):
        a, b, _ = pairs[i_connection]
        circuit = circuits.get(a, {a}) | circuits.get(b, {b})
        for node in circuit:
            circuits[node] = circuit

    flat_circuits = set(tuple(circuit) for circuit in circuits.values())
    circuits_sizes = [len(circuit) for circuit in flat_circuits]
    circuits_sizes.sort()
    return reduce(lambda a, b: a * b, circuits_sizes[-3:])


def part_2(lines: list[str]):
    positions = [
        tuple(int(number) for number in re.match(R"(\d+),(\d+),(\d+)", line).groups())
        for line in lines
    ]
    pairs = [
        (a, b, sum((xa - xb) ** 2 for xa, xb in zip(a, b)))
        for a, b in combinations(positions, 2)
    ]
    pairs.sort(key=lambda x: x[-1])

    circuits: dict[tuple[int, int, int], set[int]] = {}
    for i_connection in range(len(pairs)):
        a, b, _ = pairs[i_connection]
        circuit = circuits.get(a, {a}) | circuits.get(b, {b})
        if len(circuit) == len(positions):
            return a[0] * b[0]
        for node in circuit:
            circuits[node] = circuit
    raise Exception()


def test_part_1():
    with open("d08/example1.txt") as f:
        assert part_1(f.readlines(), 10) == 40


def test_part_2():
    with open("d08/example1.txt") as f:
        assert part_2(f.readlines()) == 25272


def main():
    with open("d08/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines, 1000))
    print(part_2(lines))


if __name__ == "__main__":
    main()
