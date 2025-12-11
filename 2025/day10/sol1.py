from collections import deque

with open("input.txt") as f_hndl:
    lines = f_hndl.readlines()


def swap_one_char(string: str, index: int, new_char: str) -> str:
    return string[:index] + new_char + string[index + 1 :]


total = 0
for line in lines:
    parts = line.strip().split(" ")
    target_diagram = parts[0].strip("[]")
    buttons = [tuple(map(int, button.strip("()").split(","))) for button in parts[1:-1]]

    start_diagram = "." * len(target_diagram)
    nb_of_presses = {start_diagram: 0}
    queue = deque([start_diagram])
    while queue:
        current_diagram = queue.popleft()
        nb_press = nb_of_presses[current_diagram]

        if current_diagram == target_diagram:
            break

        for button in buttons:
            next_diagram = current_diagram
            for swap_key in button:
                swap_char = "#" if next_diagram[swap_key] == "." else "."
                next_diagram = swap_one_char(next_diagram, swap_key, swap_char)
            new_nb_press = nb_press + 1
            if next_diagram not in nb_of_presses:
                nb_of_presses[next_diagram] = new_nb_press
                queue.append(next_diagram)

    total += nb_of_presses[target_diagram]

print(total)
