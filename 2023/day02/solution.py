import re

with open("input.txt", "r") as f_hndl:
    lines = f_hndl.readlines()


max_cubes = (12, 13, 14)  # RGB
sum_id = 0

for line in lines:
    game_id = re.match(r"Game (\d+):", line).group(1)
    reds = re.findall("(\d+) red", line)
    blues = re.findall("(\d+) blue", line)
    greens = re.findall("(\d+) green", line)

    for max_value, values in zip(max_cubes, (reds, greens, blues)):
        if sum(int(v) > max_value for v in values) > 0:
            break
    else:
        sum_id += int(game_id)

print(sum_id)
