import numpy as np

with open("input.txt") as f_hndl:
    mat = []
    moves = []
    for line in f_hndl.readlines():
        if line.startswith("#"):
            mat.append(list(line.strip()))
        elif line:
            moves += list(line.strip())

mat = np.asarray(mat)


def try_move(mat, move, x, y):
    if move == "<":
        next_cell = x, y - 1
    elif move == ">":
        next_cell = x, y + 1
    elif move == "^":
        next_cell = x - 1, y
    elif move == "v":
        next_cell = x + 1, y

    if mat[next_cell] == "O":
        mat_before = mat.copy()
        mat, success, _, _ = try_move(mat, move, *next_cell)
        if not success:
            return mat_before, False, x, y

    if mat[next_cell] == ".":
        mat[next_cell] = mat[x, y]
        mat[x, y] = "."
        return mat, True, *next_cell

    return mat, False, x, y


x, y = np.squeeze(np.where(mat == "@"))
for move in moves:
    mat, success, x, y = try_move(mat, move, x, y)

print(sum(x * 100 + y for x, y in zip(*np.where(mat == "O"))))
