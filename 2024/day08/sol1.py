from collections import defaultdict
from itertools import product

with open("input.txt") as f_hndl:
    mat = f_hndl.read().strip()

width = mat.index("\n")
mat = mat.replace("\n", "")
size = len(mat)
height = size // width


def to_coord(point):
    return point % width, point // width


freq_map = defaultdict(list)  # char: list of positions

for i, char in enumerate(mat):
    if char == ".":
        continue
    freq_map[char].append(to_coord(i))

antinodes = set()  # set of all antinode positions
for positions in freq_map.values():
    for p1, p2 in product(positions, repeat=2):
        if p1 == p2:
            continue
        vec = p2[0] - p1[0], p2[1] - p1[1]
        antinode = p2[0] + vec[0], p2[1] + vec[1]
        if (
            antinode[0] < 0
            or antinode[0] >= width
            or antinode[1] < 0
            or antinode[1] >= height
        ):
            continue
        antinodes.add(antinode)

print(len(antinodes))
