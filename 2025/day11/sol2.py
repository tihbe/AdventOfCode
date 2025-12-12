import networkx as nx
from functools import cache

G = nx.DiGraph()
with open("input.txt") as f_hndl:
    lines = f_hndl.readlines()

for line in lines:
    input_node = line[: line.index(":")]
    output_nodes = [n.strip() for n in line.split(" ")[1:]]
    G.add_nodes_from([input_node] + output_nodes)
    G.add_edges_from([(input_node, output_node) for output_node in output_nodes])

try:
    nx.find_cycle(G)
except nx.NetworkXNoCycle:
    pass
else:
    raise Exception("input.txt must be non-cyclic")


@cache
def count_path(start, end):
    if start == end:
        return 1

    return sum((count_path(neighbor, end)) for neighbor in G.neighbors(start))


svr_to_dac = count_path("svr", "dac")
svr_to_fft = count_path("svr", "fft")
fft_to_dac = count_path("fft", "dac")
dac_to_fft = count_path("dac", "fft")
fft_to_out = count_path("fft", "out")
dac_to_out = count_path("dac", "out")

print(svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out)
