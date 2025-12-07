from functools import cache

with open("input.txt") as f_hndl:
    mat = [[*line.strip()] for line in f_hndl.readlines()]
w = len(mat)
h = len(mat[0])

coo_mat = {
    (y, x): mat[x][y] for x in range(w) for y in range(h) if mat[x][y] in {"^", "S"}
}


@cache
def go_down(beam_x, pos_y):
    if pos_y < h:
        pos_y += 1

        if (beam_x, pos_y) in coo_mat:
            return go_down(beam_x - 1, pos_y) + go_down(beam_x + 1, pos_y)
        else:
            return go_down(beam_x, pos_y)
    else:
        return 1


start_x, start_y = next(key for key, value in coo_mat.items() if value == "S")

print(go_down(start_x, start_y))
