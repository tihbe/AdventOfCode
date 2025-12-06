with open("input.txt") as f:
    ranges = []

    for line in f.readlines():
        line = line.strip()
        if line:
            if "-" in line:
                ranges.append([int(x) for x in line.split("-")])

ranges.sort()

merged = [ranges[0]]
for new_start, new_end in ranges[1:]:
    if new_start > merged[-1][1] + 1:  # no overlap
        merged.append([new_start, new_end])
    else:
        merged[-1][1] = max(merged[-1][1], new_end)

tot = sum(end - start + 1 for start, end in merged)
print(tot)
