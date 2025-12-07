with open("input.txt") as f_hndl:
    mat = [[*line.strip()] for line in f_hndl.readlines()]
w = len(mat)
h = len(mat[0])

coo_mat = {
    (y, x): mat[x][y] for x in range(w) for y in range(h) if mat[x][y] in {"^", "S"}
}

start_x, pos_y = next(key for key, value in coo_mat.items() if value == "S")
beams = {start_x}
tot = 0
while pos_y < h:
    pos_y += 1
    new_beams = set()
    for beam_x in beams:
        if (beam_x, pos_y) in coo_mat:
            new_beams |= {beam_x - 1, beam_x + 1}
            tot += 1
        else:
            new_beams.add(beam_x)
    beams = new_beams

print(tot)
