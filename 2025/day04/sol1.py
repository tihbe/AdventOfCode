with open("input.txt") as f:
    x = [[*line.strip()] for line in f.readlines()]

w = len(x)
h = len(x[0])

d = {}
for i in range(w):
    for j in range(h):
        if x[i][j] == "@":
            d[i,j] = 1
tot = 0
for i, j in d.keys():
    n = 0
    n += d.get((i, j+1), 0)
    n += d.get((i, j-1), 0)
    n += d.get((i+1, j), 0)
    n += d.get((i-1, j), 0)
    n += d.get((i+1, j+1), 0)
    n += d.get((i+1, j-1), 0)
    n += d.get((i-1, j+1), 0)
    n += d.get((i-1, j-1), 0)
    if n < 4:
        tot += 1

print(tot)