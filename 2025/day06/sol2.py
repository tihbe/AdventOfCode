import numpy as np

ops = {"*": np.prod, "+": np.sum}

mat = {}
with open("input.txt") as f:
    lines = f.readlines()
    n_lines = len(lines)
    max_line_length = 0
    for line_number, line in enumerate(lines):
        for char_pos, char in enumerate(line.rstrip("\r\n")):
            mat[line_number, char_pos] = char
            max_line_length = max(char_pos, max_line_length)


operators = [
    (row_nb, ops[op]) for row_nb, op in enumerate(lines[-1]) if op in ops.keys()
]
operators.append([max_line_length + 2, None])

tot = 0
for (start_row, operator), (end_row, _) in zip(operators[:-1], operators[1:]):
    numbers = []
    for j in range(start_row, end_row - 1):
        nb = "".join(mat.get((i, j), 0) for i in range(n_lines - 1))
        numbers.append(int(nb))
    tot += operator(numbers)

print(tot)
