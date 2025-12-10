from itertools import combinations


def part_1(lines: list[str]):
    corners = [tuple(int(n) for n in line.split(",")) for line in lines]
    return max(
        (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)
        for corner_1, corner_2 in combinations(corners, 2)
    )


def part_2(lines: list[str]):
    """
    This solution is not general, a rectangle that lies totally outside of the red and green tiles will pass this check.
    The general solution should be to construct two clockwise loops, for the red-green tiles area and the rectangle respectively,
    and check for the overlapped edge tiles whether the red-green tiles area edge is not 90 deg counter-clockwide turn from the rectangle edge.
    """
    corners = [tuple(int(n) for n in line.split(",")) for line in lines]
    x_mapping = {
        x: 2 * sx for sx, x in enumerate(sorted(set(corner[0] for corner in corners)))
    }
    y_mapping = {
        y: 2 * sy for sy, y in enumerate(sorted(set(corner[1] for corner in corners)))
    }
    mapped_corners = [(x_mapping[x], y_mapping[y]) for x, y in corners]
    mapped_edges = set()
    for from_mapped_corner, to_mapped_corner in zip(
        mapped_corners, mapped_corners[1:] + mapped_corners[:1]
    ):
        x_i, y_i = from_mapped_corner
        x_f, y_f = to_mapped_corner
        if x_i == x_f:
            mapped_edges.update(
                (x_i, y) for y in range(min(y_i, y_f), max(y_i, y_f) + 1)
            )
        else:
            mapped_edges.update(
                (x, y_i) for x in range(min(x_i, x_f), max(x_i, x_f) + 1)
            )

    def is_valid(corner_1, corner_2):
        x1, y1 = x_mapping[corner_1[0]], y_mapping[corner_1[1]]
        x2, y2 = x_mapping[corner_2[0]], y_mapping[corner_2[1]]
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for iy in range(y1 + 1, y2):
            for ix in range(x1 + 1, x2):
                if (ix, iy) in mapped_edges:
                    return False
        return True

    return max(
        (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)
        for corner_1, corner_2 in combinations(corners, 2)
        if is_valid(corner_1, corner_2)
    )


def test_part_1():
    with open("d09/example1.txt") as f:
        assert part_1(f.readlines()) == 50


def test_part_2():
    with open("d09/example1.txt") as f:
        assert part_2(f.readlines()) == 24


def main():
    with open("d09/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
