import heapq
from collections import defaultdict

with open("input.txt") as f_hndl:
    pairs = [line.strip().split("-") for line in f_hndl.readlines()]

graph = defaultdict(set)
for x, y in pairs:
    graph[x].add(y)
    graph[y].add(x)


min_cost = float("inf")
best_path = None
for start_node in graph.keys():
    tovisit = [(-1, start_node, set((start_node,)))]
    min_cost_for_node = float("inf")
    while tovisit:
        cost, node, visited = heapq.heappop(tovisit)
        if cost > min_cost_for_node:
            break
        min_cost_for_node = min(min_cost_for_node, cost)
        if min_cost_for_node <= min_cost:
            min_cost = min_cost_for_node
            best_path = visited
        neighbors = graph[node] - visited
        for next_node in neighbors:
            relations = graph[next_node].intersection(visited)
            if len(relations) != len(visited):
                continue
            heapq.heappush(tovisit, (cost - 1, next_node, visited | set((next_node,))))


print(",".join(sorted(best_path)))
