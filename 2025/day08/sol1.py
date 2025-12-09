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

G.add_nodes_from(range(len(mat)))

for _ in range(1000):
    _, i, j = distances.pop(0)
    G.add_edge(i, j)

sizes = sorted(len(x) for x in nx.connected_components(G))
print(np.prod(sizes[-3:]))
