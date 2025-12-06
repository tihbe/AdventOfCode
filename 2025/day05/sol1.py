with open("input.txt") as f:
    ranges = []
    ingredients = []
    for line in f.readlines():
        line = line.strip()
        if line:
            if "-" in line:
                ranges.append([int(x) for x in line.split("-")])
            else:
                ingredients.append(int(line))

tot = 0

for ingredient in ingredients:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            tot += 1
            break

print(tot)
