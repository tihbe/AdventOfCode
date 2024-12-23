from collections import defaultdict


with open("input.txt") as f_hndl:
    pairs = [line.strip().split("-") for line in f_hndl.readlines()]

graph = defaultdict(list)
for x, y in pairs:
    graph[x].append(y)
    graph[y].append(x)


def recurse(root, size, node=None, visited=set()):
    if node == root and size == 0:
        return [tuple(sorted(visited))]
    if node is None:
        node = root
    if size == 0 or node in visited:
        return []

    visited = visited | set((node,))

    subgraphs = []
    for con in graph[node]:
        subgraphs += recurse(root, size - 1, con, visited)

    return subgraphs


total = 0
subgraphs = list()
for node in graph.keys():
    if node[0] == "t":
        subgraphs += recurse(node, 3)
print(len(set(subgraphs)))
