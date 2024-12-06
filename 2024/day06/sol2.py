from itertools import cycle
from tqdm import trange

with open("input.txt") as f_hndl:
    mat = f_hndl.read().strip()
width = mat.index("\n")
mat = mat.replace("\n", "")
size = len(mat)
height = size // width


def to_coord(point):
    return point % width, point // width


total = 0
obstacles = set(to_coord(i) for i, char in enumerate(mat) if char == "#")
starting_pos = to_coord(mat.find("^"))

for i in trange(size):
    if mat[i] in {"#", "^"}:
        continue

    iter_obstacles = obstacles.copy()
    iter_obstacles.add(to_coord(i))

    pos = starting_pos
    route = set()
    next_dir = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))
    dir = next(next_dir)
    seen_cntr = 0

    while True:
        route.add(pos)
        next_pos = pos[0] + dir[0], pos[1] + dir[1]
        if next_pos[0] < 0 or next_pos[0] >= width:
            break  # nice exit
        if next_pos[1] < 0 or next_pos[1] >= height:
            break  # nice exit
        if next_pos in iter_obstacles:
            dir = next(next_dir)
            continue
        pos = next_pos

        if pos in route:
            seen_cntr += 1
        else:
            seen_cntr = 0

        if seen_cntr >= size:  # in a loop
            # could be >= 2 if direction is the same
            total += 1
            break

print(total)
