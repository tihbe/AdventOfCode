import re

# New pure python solution now that I know what is a "picture of a christmas tree" :-D

width = 101
height = 103

with open("input.txt") as f_hndl:
    positions = re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", f_hndl.read())


duration = 0
while True:
    mat = [0 for _ in range(height * width)]
    for guard in positions:
        x, y, vx, vy = map(int, guard)
        fx = (x + vx * duration) % width
        fy = (y + vy * duration) % height
        mat[fx * width + fy] += 1

    diff = [v1 - v2 for v1, v2 in zip(mat[:-1], mat[1:])]
    val = sum(d == 0 for d, v in zip(diff, mat) if v != 0) / len(diff)
    # Tree is dense, so shift pixels by 1 and measure diff where there is a non-zero pixel
    if val > 0.01:
        print(duration)
        break
    duration += 1
