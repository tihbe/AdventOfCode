import numpy as np
import heapq
from collections import namedtuple

with open("input.txt") as f_hndl:
    mat = np.array([list(line.strip()) for line in f_hndl.readlines()])

width, height = mat.shape
start_x, start_y = np.squeeze(np.where(mat == "S"))

Move = namedtuple("Move", ["cost", "x", "y", "dx", "dy"])

moves = [Move(0, start_x, start_y, 0, 1)]
visited = {(start_x, start_y): 0}  # pos: cost

while moves:
    last_move = heapq.heappop(moves)
    if mat[last_move.x, last_move.y] == "E":
        print(last_move.cost)  # Success
        break
    for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
        next_x, next_y = last_move.x + dx, last_move.y + dy
        if next_x < 0 or next_x >= width:
            continue
        if next_y < 0 or next_y >= height:
            continue
        if mat[next_x, next_y] == "#":
            continue
        same_direction = dx == last_move.dx and dy == last_move.dy
        next_cost = (1 if same_direction else 1001) + last_move.cost
        if (next_x, next_y) in visited and visited[next_x, next_y] <= next_cost:
            continue
        visited[next_x, next_y] = next_cost
        next_move = Move(next_cost, next_x, next_y, dx, dy)
        heapq.heappush(moves, next_move)
