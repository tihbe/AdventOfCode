import numpy as np
from itertools import combinations
import networkx as nx
# lazy day ¯\_(ツ)_/¯

mat = np.loadtxt("input.txt", delimiter=",")
G = nx.Graph()
distances = []
for i, j in combinations(range(len(mat)), 2):
    distances.append((np.linalg.norm(mat[i] - mat[j]), i, j))
distances.sort()

seen = set()
while distances:
    _, i, j = distances.pop(0)
    seen |= {i, j}
    if len(seen) == len(mat):
        print(int(mat[i][0] * mat[j][0]))
        break
