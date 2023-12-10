import numpy as np
from scipy.signal import convolve2d

with open("input.txt", "r") as f_hndl:
    lines = f_hndl.readlines()

grid = np.array([[char for char in line.strip()] for line in lines])
symbol_mask = ~(
    np.char.isdigit(grid) | (grid == ".")
)  # true if position is a symbol other than "."
kernel = np.ones((3, 3))
valid_mask = convolve2d(symbol_mask, kernel, "same") > 0
total = 0
for x, line in enumerate(grid):
    previous_char = None
    current_number = ""
    valid_number = False
    for y, c in enumerate(line):
        if c.isdigit():
            current_number += c
            if valid_mask[x, y]:
                valid_number = True

        elif current_number != "":
            if valid_number:
                total += int(current_number)
            current_number = ""
            valid_number = False
    if valid_number:
        total += int(current_number)

print(total)
