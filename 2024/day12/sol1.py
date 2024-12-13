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
perim = defaultdict(int)
for i in range(width):
    for j in range(height):
        region = mat[i][j]
        area[region] += 1
        perim[region] += i == 0 or mat[i - 1][j] != region
        perim[region] += j == 0 or mat[i][j - 1] != region
        perim[region] += i == width - 1 or mat[i + 1][j] != region
        perim[region] += j == height - 1 or mat[i][j + 1] != region

print(sum(area[key] * perim[key] for key in area.keys()))
