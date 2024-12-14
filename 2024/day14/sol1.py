import re

width = 101
height = 103
duration = 100
with open("input.txt") as f_hndl:
    positions = re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", f_hndl.read())

quadrants = [0] * 4

for guard in positions:
    x, y, vx, vy = map(int, guard)
    fx = (x + vx * duration) % width
    fy = (y + vy * duration) % height
    left_q = fx < width // 2
    right_q = fx >= width - width // 2
    higher_q = fy < height // 2
    lower_q = fy >= height - height // 2
    quadrants[0] += left_q and higher_q
    quadrants[1] += left_q and lower_q
    quadrants[2] += right_q and higher_q
    quadrants[3] += right_q and lower_q

total = 1
for q in quadrants:
    total *= q
print(total)
