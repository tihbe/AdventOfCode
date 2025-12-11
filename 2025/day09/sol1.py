from itertools import combinations

with open("input.txt") as f_hndl:
    values = [tuple(map(int, line.strip().split(","))) for line in f_hndl.readlines()]

rectangles = list(combinations(range(len(values)), 2))
areas = [
    (1 + abs(values[r1][0] - values[r2][0])) * (1 + abs(values[r1][1] - values[r2][1]))
    for r1, r2 in rectangles
]

sorted_idx = list(sorted(range(len(rectangles)), key=areas.__getitem__))

print(areas[sorted_idx[-1]])
