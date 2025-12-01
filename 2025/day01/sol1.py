with open("input.txt") as f:
    lines = f.read().splitlines()

dial = 50
zero_cntr = 0
for line in lines:
    direction = line[0]
    value = int(line[1:])
    if direction == "R":
        dial = (dial + value) % 100
    elif direction == "L":
        dial = (dial - value) % 100

    zero_cntr += dial == 0

print(zero_cntr)
