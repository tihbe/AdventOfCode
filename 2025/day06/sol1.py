import numpy as np

ops = {"*": np.prod, "+": np.sum}
mat = np.loadtxt("input.txt", dtype=object)

tot = 0
for row in mat.T:
    op = row[-1]
    values = row[:-1].astype(int)
    tot += ops[op](values)

print(tot)
