from itertools import cycle

with open("input.txt") as f_hndl:
    mat = f_hndl.read().strip()

width = mat.index("\n")
mat = mat.replace("\n", "")
size = len(mat)
height = size // width


def to_coord(point):
    return point % width, point // width


pos = to_coord(mat.find("^"))
obstacles = set(to_coord(i) for i, char in enumerate(mat) if char == "#")
route = set()

next_dir = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))
dir = next(next_dir)

while True:
    route.add(pos)
    next_pos = pos[0] + dir[0], pos[1] + dir[1]
    if next_pos[0] < 0 or next_pos[0] >= width:
        break
    if next_pos[1] < 0 or next_pos[1] >= height:
        break
    if next_pos in obstacles:
        dir = next(next_dir)
        continue
    pos = next_pos

print(len(route))
