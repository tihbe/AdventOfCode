import re

with open("input.txt") as f_hndl:
    data = f_hndl.read()
groups = re.findall("mul\((\d+),(\d+)\)", data)
print(sum(int(x) * int(y) for x, y in groups))
