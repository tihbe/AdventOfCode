with open("input.txt") as f:
    lines = f.read().splitlines()

dial = 50
zero_cntr = 0
for line in lines:
    direction = line[0]
    value = int(line[1:])

    # Full rotations
    zero_cntr += value // 100
    value %= 100

    if direction == "L":
        value = -value

    next_dial = dial + value
    if next_dial > 100:
        zero_cntr += 1
    elif next_dial < 0 and dial > 0:
        zero_cntr += 1

    next_dial %= 100
    if next_dial == 0:
        zero_cntr += 1

    dial = next_dial

print(zero_cntr)
