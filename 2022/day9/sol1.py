import numpy as np

with open("input.txt", "r") as f_hndl:
    head_position = [0, 0]
    tail_position = (0, 0)
    tail_position_history = set()
    for line in f_hndl:
        direction, movement_size = line.split()
        movement_size = int(movement_size)

        for i in range(movement_size):
            start_position = head_position.copy()

            if direction == "R":
                head_position[0] += 1
            elif direction == "L":
                head_position[0] -= 1
            elif direction == "U":
                head_position[1] += 1
            elif direction == "D":
                head_position[1] -= 1

            dx = head_position[0] - tail_position[0]
            dy = head_position[1] - tail_position[1]
            if abs(dx) > 1 or abs(dy) > 1:
                tail_position = (tail_position[0] + np.sign(dx), tail_position[1] + np.sign(dy))

            tail_position_history.add(tail_position)

    print(len(tail_position_history))
