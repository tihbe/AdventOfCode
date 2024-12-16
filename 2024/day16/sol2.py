import numpy as np
import heapq
from collections import namedtuple


with open("input.txt") as f_hndl:
    mat = np.array([list(line.strip()) for line in f_hndl.readlines()])


width, height = mat.shape
start_x, start_y = np.squeeze(np.where(mat == "S"))

Move = namedtuple("Move", ["cost", "x", "y", "dx", "dy", "hist"])

moves = [Move(0, start_x, start_y, 0, 1, [(start_x, start_y)])]
visited = {(start_x, start_y): 0}  # pos: cost
best_cost = None
successful_paths = []

while moves:
    last_move = heapq.heappop(moves)
    if best_cost is not None and last_move.cost > best_cost:
        break  # done
    if mat[last_move.x, last_move.y] == "E":
        best_cost = last_move.cost
        successful_paths.append(last_move.hist)
        continue
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
        if (next_x, next_y) in last_move.hist:
            continue
        if (next_x, next_y) in visited and visited[(next_x, next_y)] + 1001 < next_cost:
            continue

        visited[next_x, next_y] = next_cost
        next_move = Move(
            next_cost, next_x, next_y, dx, dy, [*last_move.hist, (next_x, next_y)]
        )
        heapq.heappush(moves, next_move)


chairs = set()
for sp in successful_paths:
    chairs = chairs.union(sp)
print(len(chairs))


# display just for fun
try:
    import cv2

    display_mat = cv2.cvtColor(np.zeros_like(mat, dtype=np.uint8), cv2.COLOR_GRAY2BGR)
    display_mat[mat == "#"] = (0, 0, 0)
    display_mat[mat != "#"] = (255, 255, 255)
    for x, y in chairs:
        display_mat[x, y] = (0, 127, 255)

    display_mat = cv2.resize(
        display_mat,
        (780, int(780 * height / width)),
        interpolation=cv2.INTER_NEAREST_EXACT,
    )

    cv2.imshow("lab", display_mat)
    cv2.waitKey(0)
except ImportError:
    pass
