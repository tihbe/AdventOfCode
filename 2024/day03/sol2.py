import re

with open("input.txt") as f_hndl:
    data = f_hndl.read()
groups = re.findall("(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", data)

active = True
total = 0
for grp in groups:
    x, y, do, dont = grp
    if do:
        active = True
    elif dont:
        active = False
    elif active:
        total += int(x) * int(y)

print(total)
