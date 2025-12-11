from itertools import combinations
from shapely.geometry import Polygon, box

with open("input.txt") as f_hndl:
    values = [tuple(map(int, line.strip().split(","))) for line in f_hndl.readlines()]

rectangles = list(combinations(range(len(values)), 2))
areas = [
    (1 + abs(values[r1][0] - values[r2][0])) * (1 + abs(values[r1][1] - values[r2][1]))
    for r1, r2 in rectangles
]

sorted_idx = list(sorted(range(len(rectangles)), key=areas.__getitem__))

polygon = Polygon([*values, values[0]])

while sorted_idx:
    max_rect_id = sorted_idx.pop()
    p1, p2 = rectangles[max_rect_id]
    x1, y1 = values[p1]
    x2, y2 = values[p2]

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    rect = box(x1, y1, x2, y2)

    if polygon.contains(rect):
        print(areas[max_rect_id])
        break
