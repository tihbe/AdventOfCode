import re

with open("input.txt") as f_hndl:
    data = f_hndl.read().strip().split(",")

values = [
    tuple(int(x) for x in part.split("-")) for part in data 
]

regex = re.compile(r"^(\d+)\1+$")

total = 0
for range_start, range_end in values:
    for nb in range(range_start, range_end+1):
        nb_str = str(nb)
        if regex.match(nb_str):
            total += nb

print(total)
