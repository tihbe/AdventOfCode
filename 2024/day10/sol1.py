import numpy as np

with open("input.txt") as f_hndl:
    mat = np.array(
        [
            [int(-1 if i == "." else i) for i in line.strip()]
            for line in f_hndl.readlines()
        ]
    )

width, height = mat.shape
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def climb(x, y):
    level = mat[x, y]

    if level == 9:
        return {(x, y)}

    total = set()
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if next_x < 0 or next_y < 0 or next_x >= width or next_y >= height:
            continue
        if mat[next_x, next_y] == level + 1:
            total |= climb(next_x, next_y)

    return total


start_x, start_y = np.where(mat == 0)
total = sum(len(climb(x, y)) for x, y in zip(start_x, start_y))
print(total)
