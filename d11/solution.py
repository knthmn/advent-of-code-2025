import re


def parse(lines: list[str]):
    nodes = {}
    for line in lines:
        node, outputs = re.match(R"([a-z]+):\s([a-z\s]+)", line).groups()
        outputs = outputs.strip().split(" ")
        nodes[node] = outputs
    return nodes


def part_1(lines: list[str]):
    nodes = parse(lines)
    return find_num_paths(nodes, "you", "out")[0]


def find_num_paths(nodes, start, to, stop_search=None):
    if stop_search is None:
        stop_search = set()
    heads = [start]
    num_paths = 0
    visted_nodes = set()
    while heads:
        head = heads.pop()
        next_nodes = nodes.get(head, [])
        for next_node in next_nodes:
            visted_nodes.add(next_node)
            if next_node in stop_search:
                continue
            if next_node == to:
                num_paths += 1
            else:
                heads.append(next_node)
    return num_paths, visted_nodes


def part_2(lines: list[str]):
    nodes = parse(lines)
    # for both the example and my input, it goes from input -> fft -> dac -> out
    num_dac_paths, after_dac_section = find_num_paths(nodes, "dac", "out")
    num_fft_paths, after_fft_section = find_num_paths(
        nodes, "fft", "dac", after_dac_section
    )
    num_svr_paths, _ = find_num_paths(
        nodes, "svr", "fft", after_dac_section | after_fft_section
    )
    return num_dac_paths * num_fft_paths * num_svr_paths


def test_part_1():
    with open("d11/example1.txt") as f:
        assert part_1(f.readlines()) == 5


def test_part_2():
    with open("d11/example2.txt") as f:
        assert part_2(f.readlines()) == 2


def main():
    with open("d11/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
