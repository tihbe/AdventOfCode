with open("input.txt", "r") as f_hndl:
    lines = f_hndl.readlines()


def find_digit(line, reversed=False):
    if reversed:
        line = line[::-1]
    for i, c in enumerate(line):
        if c.isdigit():
            return c
        else:
            for nb, val in enumerate(
                [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ]
            ):
                if reversed:
                    val = val[::-1]
                if val in line[: i + 1]:
                    return str(nb + 1)


total = 0
for line in lines:
    digits = find_digit(line) + find_digit(line, reversed=True)
    total += int(digits)

print(total)
