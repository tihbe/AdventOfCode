import heapq
from collections import namedtuple

with open("input.txt") as f_hndl:
    falling_bytes = [
        tuple(int(x) for x in line.split(","))
        for line in f_hndl.readlines()
        if len(line) > 2
    ]

# same solution as day16, replacing the matrix by a set of "wall" positions

width, height = 71, 71

for i in range(1024, len(falling_bytes)):
    corrupted_mem = set(falling_bytes[:i])
    start_x, start_y = (0, 0)

    Move = namedtuple("Move", ["cost", "x", "y"])

    moves = [Move(0, start_x, start_y)]
    visited = {(start_x, start_y): 0}  # pos: cost
    while moves:
        last_move = heapq.heappop(moves)
        if (last_move.x, last_move.y) == (70, 70):
            break
        for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            next_x, next_y = last_move.x + dx, last_move.y + dy
            if next_x < 0 or next_x >= width:
                continue
            if next_y < 0 or next_y >= height:
                continue

            next_cost = 1 + last_move.cost

            if (next_x, next_y) in corrupted_mem:
                continue

            if (next_x, next_y) in visited and visited[next_x, next_y] <= next_cost:
                continue
            visited[next_x, next_y] = next_cost
            next_move = Move(next_cost, next_x, next_y)
            heapq.heappush(moves, next_move)
    else:
        print("{},{}".format(*falling_bytes[i - 1]))
        break
