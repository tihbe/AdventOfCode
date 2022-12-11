import numpy as np


def follow(movements):
    tail_position = (0, 0)
    tail_position_history = []
    for head_position in movements:
        dx = head_position[0] - tail_position[0]
        dy = head_position[1] - tail_position[1]

        if abs(dx) > 1 or abs(dy) > 1:
            tail_position = (tail_position[0] + np.sign(dx), tail_position[1] + np.sign(dy))

        tail_position_history.append(tail_position)

    return tail_position_history


with open("input.txt", "r") as f_hndl:
    movements = []
    head_position = [0, 0]
    for line in f_hndl:
        direction, movement_size = line.split()
        for i in range(int(movement_size)):
            start_position = head_position.copy()
            if direction == "R":
                head_position[0] += 1
            elif direction == "L":
                head_position[0] -= 1
            elif direction == "U":
                head_position[1] += 1
            elif direction == "D":
                head_position[1] -= 1

            movements.append(tuple(head_position))

    tail_position_history = movements
    for i in range(nb_of_knots := 9):
        tail_position_history = follow(tail_position_history)

    unique_position_history = set(tail_position_history)

    print(len(unique_position_history))
