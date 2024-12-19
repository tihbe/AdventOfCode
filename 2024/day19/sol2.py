from bisect import bisect_left
from functools import lru_cache

with open("input.txt") as f_hndl:
    designs = []
    for line in f_hndl.readlines():
        line = line.strip()
        if "," in line:
            patterns = line.split(", ")
        elif len(line) > 0:
            designs.append(line)


patterns = list(sorted(patterns))


@lru_cache(None)
def is_possible(design: str):
    if len(design) == 0:
        return 1

    possible_design_count = 0
    # get subset of patterns that start with the same letter
    start_idx = max(bisect_left(patterns, design[0]) - 1, 0)
    end_idx = bisect_left(patterns, chr(ord(design[0]) + 1))
    for pattern in patterns[start_idx:end_idx]:
        if design.startswith(pattern):
            possible_design_count += is_possible(design[len(pattern) :])

    return possible_design_count


design_count = sum(is_possible(design) for design in designs)
print(design_count)
