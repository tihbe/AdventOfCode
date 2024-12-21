from functools import lru_cache

with open("input.txt") as f_hndl:
    codes = [line.strip() for line in f_hndl.readlines()]


numeric_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
    "D": (0, 3),  # dead
}
direction_keypad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
    "D": (0, 0),  # dead
}
move_map = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def get_all_paths(keypad, p1, p2):
    """Return all possible movements from p1 to p2 that are not in dead zone"""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    possible_movements = [
        # either we do horizontal first, or vertical first
        # never cost-efficient to alternate
        -dy * "^" + dy * "v" + -dx * "<" + dx * ">",
        -dx * "<" + dx * ">" + -dy * "^" + dy * "v",
    ]
    if dx == 0 or dy == 0:
        possible_movements = possible_movements[:1]

    for directions in possible_movements:
        x, y = p1
        for move in directions:
            dx, dy = move_map[move]
            x, y = x + dx, y + dy
            if (x, y) == keypad["D"]:
                break
        else:
            yield directions


def get_code(keypad, code):
    pos = keypad["A"]
    directions = []
    for letter in code:
        next_pos = keypad[letter]
        if pos == next_pos:
            directions.append("A")
            continue

        possible_paths = list(get_all_paths(keypad, pos, next_pos))

        if len(possible_paths) == 1:
            directions.append(possible_paths[0] + "A")
        else:
            directions.append([pp + "A" for pp in possible_paths])
        pos = next_pos
    return directions


def generate_combinations(input_list):
    combinations = [""]

    for element in input_list:
        new_combinations = []
        if isinstance(element, str):
            for combo in combinations:
                new_combinations.append(combo + element)
        else:
            for combo in combinations:
                for item in element:
                    new_combinations.append(combo + item)

        combinations = new_combinations

    return combinations


@lru_cache(None)
def recurse(size, p_previous):
    if size == 0:
        return len(p_previous)

    length = 0
    for code in get_code(direction_keypad, p_previous):
        if isinstance(code, str):
            length += recurse(size - 1, code)
        else:
            length += min(recurse(size - 1, c) for c in code)

    return length


total = 0
for code in codes:
    min_length = float("inf")
    numeric_choices = generate_combinations(get_code(numeric_keypad, code))
    for phuman in numeric_choices:
        min_length = min(min_length, recurse(25, phuman))

    numeric_part = int("".join(c for c in code if c.isnumeric()))
    total += min_length * numeric_part

print(total)
