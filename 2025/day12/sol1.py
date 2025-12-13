import numpy as np

with open("input.txt") as f_hndl:
    parts = f_hndl.read().split("\n\n")

puzzles = parts[-1]
gifts = parts[:-1]

gift_d = {}

for gift in gifts:
    lines = gift.split("\n")
    id = int(lines[0].split(":")[0])
    schema = lines[1:]
    gift_d[id] = np.asarray([[*string] for string in schema]) == "#"

puzzle_def = []
for puzzle in puzzles.splitlines():
    size, counts = puzzle.split(": ")
    width, height = size.split("x")
    puzzle_def.append(
        {
            "width": int(width),
            "height": int(height),
            "counts": np.asarray(tuple(map(int, counts.split(" ")))),
        }
    )

tot = 0
for puzzle in puzzle_def:
    to_add = []
    for i, cnt in enumerate(puzzle["counts"]):
        to_add += [gift_d[i]] * cnt
    to_add = np.asarray(to_add)
    area = puzzle["width"] * puzzle["height"]

    # Too many '#' to even fit
    if np.sum(to_add) >= area:
        continue

    # Fits no matter the shape
    if np.prod(to_add.shape) <= area:
        tot += 1
        continue

    raise Exception("Do I even need to continue??")  # lol

print(tot)
