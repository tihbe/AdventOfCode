with open("input.txt") as f_hndl:
    schematics = []
    values = f_hndl.read().split("\n\n")
    for value in values:
        schematics.append([list(r) for r in value.splitlines()])

keys_col_counts = []
locks_col_counts = []
for schematic in schematics:
    col_count = [0] * 5
    for i in range(5):
        for j in range(7):
            col_count[i] += schematic[j][i] == "#"

    target = keys_col_counts if schematic[0][0] == "." else locks_col_counts
    target.append(col_count)


total = 0
for key in keys_col_counts:
    for lock in locks_col_counts:
        total += all(x + y <= 7 for x, y in zip(key, lock))
print(total)
