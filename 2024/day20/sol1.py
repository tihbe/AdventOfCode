from collections import namedtuple
from itertools import product
import heapq
import numpy as np

with open("input.txt") as f_hndl:
    mat = np.array([list(line.strip()) for line in f_hndl.readlines()])
width, height = mat.shape

Move = namedtuple("Move", ["cost", "x", "y", "hist"])
start_x, start_y = np.squeeze(np.where(mat == "S"))


def dijkstra(mat):
    moves = [Move(0, start_x, start_y, [(start_x, start_y)])]
    visited = {(start_x, start_y): 0}  # pos: cost

    while moves:
        last_move = heapq.heappop(moves)
        if mat[last_move.x, last_move.y] == "E":
            return last_move.hist  # Success
        for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            next_x, next_y = last_move.x + dx, last_move.y + dy
            if next_x < 0 or next_x >= width:
                continue
            if next_y < 0 or next_y >= height:
                continue
            if mat[next_x, next_y] == "#":
                continue
            next_cost = 1 + last_move.cost
            if (next_x, next_y) in visited and visited[next_x, next_y] <= next_cost:
                continue
            visited[next_x, next_y] = next_cost
            next_move = Move(
                next_cost, next_x, next_y, last_move.hist + [(next_x, next_y)]
            )
            heapq.heappush(moves, next_move)

    return None


# find path using day 16 dijkstra algo
path = dijkstra(mat)
positions = {p: i for i, p in enumerate(path)}
total = 0
dxs = [
    (dx, dy)
    for dx, dy in product((-2, -1, 0, 1, 2), repeat=2)
    if abs(dx) + abs(dy) <= 2 and not (dx == 0 and dy == 0)
]
for p, step in positions.items():
    for dx, dy in dxs:
        next_p = p[0] + dx, p[1] + dy
        cheat_cost = abs(dx) + abs(dy)
        if next_p in positions and positions[next_p] - step - cheat_cost >= 100:
            total += 1

print(total)
