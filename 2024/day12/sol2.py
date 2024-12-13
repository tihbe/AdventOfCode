from collections import defaultdict

with open("input.txt") as f_hndl:
    mat = [list(line.strip()) for line in f_hndl.readlines()]

width = len(mat)
height = len(mat[0])


def flood_fill(i, j, original_value, new_value):
    if i < 0 or j < 0 or i >= width or j >= height:
        return

    if mat[i][j] == original_value:
        mat[i][j] = new_value
        flood_fill(i - 1, j, original_value, new_value)
        flood_fill(i, j - 1, original_value, new_value)
        flood_fill(i + 1, j, original_value, new_value)
        flood_fill(i, j + 1, original_value, new_value)


area_cntr = 0
for i in range(width):
    for j in range(height):
        if isinstance(mat[i][j], str):
            flood_fill(i, j, mat[i][j], area_cntr)
            area_cntr += 1

area = defaultdict(int)
for i in range(width):
    for j in range(height):
        area[mat[i][j]] += 1


sides = defaultdict(int)


def add_sides_if_not_touching(region_and_positions):
    for region, positions in region_and_positions.items():
        sides[region] += len(positions) > 0
        for x1, x2 in zip(positions[:-1], positions[1:]):
            sides[region] += abs(x1 - x2) > 1


for i in range(width):
    current_sides = defaultdict(list)
    for j in range(height):
        if i == 0 or mat[i - 1][j] != mat[i][j]:
            current_sides[mat[i][j]].append(j)
    add_sides_if_not_touching(current_sides)

for j in range(height):
    current_sides = defaultdict(list)
    for i in range(width):
        if j == 0 or mat[i][j - 1] != mat[i][j]:
            current_sides[mat[i][j]].append(i)
    add_sides_if_not_touching(current_sides)

for i in range(width - 1, -1, -1):
    current_sides = defaultdict(list)
    for j in range(height - 1, -1, -1):
        if i == width - 1 or mat[i + 1][j] != mat[i][j]:
            current_sides[mat[i][j]].append(j)
    add_sides_if_not_touching(current_sides)

for j in range(height - 1, -1, -1):
    current_sides = defaultdict(list)
    for i in range(width - 1, -1, -1):
        if j == height - 1 or mat[i][j + 1] != mat[i][j]:
            current_sides[mat[i][j]].append(i)
    add_sides_if_not_touching(current_sides)

print(sum(area[key] * sides[key] for key in area.keys()))
