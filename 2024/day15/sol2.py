import numpy as np

with open("input.txt") as f_hndl:
    mat = []
    moves = []
    for line in f_hndl.readlines():
        if line.startswith("#"):
            line = (
                line.replace(".", "..")
                .replace("#", "##")
                .replace("O", "[]")
                .replace("@", "@.")
            )
            mat.append(list(line.strip()))
        elif line:
            moves += list(line.strip())

mat = np.asarray(mat)


def try_move(mat, move, x, y):
    is_vertical_move = False
    if move == "<":
        next_cell = x, y - 1
    elif move == ">":
        next_cell = x, y + 1
    elif move == "^":
        is_vertical_move = True
        next_cell = x - 1, y
    elif move == "v":
        is_vertical_move = True
        next_cell = x + 1, y

    if mat[next_cell] in {"[", "]"}:
        mat_before = mat.copy()
        if is_vertical_move:
            # if vertical, move both parts of the box
            dy = 1 if mat[next_cell] == "[" else -1
            mat, success1, _, _ = try_move(mat, move, *next_cell)
            mat, success2, _, _ = try_move(mat, move, next_cell[0], next_cell[1] + dy)
            if not (success1 and success2):
                return mat_before, False, x, y
        else:
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

print(sum(x * 100 + y for x, y in zip(*np.where(mat == "["))))
