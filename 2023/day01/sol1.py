with open("input.txt", "r") as f_hndl:
    lines = f_hndl.readlines()

total = 0
for line in lines:
    digits = ""
    for c in line:
        if c.isdigit():
            digits += c
            break
    for c in reversed(line):
        if c.isdigit():
            digits += c
            break
    total += int(digits)

print(total)
