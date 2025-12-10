import re
from collections import deque

import pulp


def parse(line: str):
    lights, buttons, joltage = re.match(
        R"\[(.*)\]\s(.*)\s{(.*)}", line.strip()
    ).groups()
    buttons = [button[1:-1] for button in buttons.split(" ")]
    buttons = [tuple(int(n) for n in button.split(",")) for button in buttons]
    joltage = tuple(int(n) for n in joltage.split(","))
    return lights, buttons, joltage


def part_1(lines: list[str]):
    s = 0

    for line in lines:
        target_light, buttons, _ = parse(line)

        def find_min_num_presses(target_lights, buttons):
            states = {"." * len(target_lights): 0}
            states_to_check = deque([next(iter(states))])
            while states_to_check:
                state = states_to_check.popleft()
                num_step = states[state]
                for button in buttons:
                    new_state = [c for c in state]
                    for loc in button:
                        new_state[loc] = "." if new_state[loc] == "#" else "#"
                    new_state = "".join(new_state)
                    if new_state == target_lights:
                        return num_step + 1
                    if new_state not in states:
                        states[new_state] = num_step + 1
                        states_to_check.append(new_state)
            raise Exception("Not found")

        s += find_min_num_presses(target_light, buttons)

    return s


def part_2(lines: list[str]):
    s = 0

    for line in lines:
        _, buttons, target_joltage = parse(line)

        def find_min_num_presses(target_joltage, buttons):
            prob = pulp.LpProblem("Problem", pulp.LpMinimize)
            num_presses = pulp.LpVariable.dicts(
                "NumPress", (range(len(buttons)),), cat="Integer"
            )
            prob += pulp.lpSum(num_presses)
            for i in range(len(buttons)):
                prob += num_presses[i] >= 0
            for joltage_idx in range(len(target_joltage)):
                button_idxs = [
                    button_idx
                    for button_idx in range(len(buttons))
                    if joltage_idx in buttons[button_idx]
                ]
                prob += target_joltage[joltage_idx] == pulp.lpSum(
                    [num_presses[button_idx] for button_idx in button_idxs]
                )
            prob.solve(pulp.PULP_CBC_CMD(msg=False))
            return int(prob.objective.value())

        s += find_min_num_presses(target_joltage, buttons)

    return s


def test_part_1():
    with open("d10/example1.txt") as f:
        assert part_1(f.readlines()) == 7


def test_part_2():
    with open("d10/example1.txt") as f:
        assert part_2(f.readlines()) == 33


def main():
    with open("d10/input.txt") as f:
        lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))


if __name__ == "__main__":
    main()
