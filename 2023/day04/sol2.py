import numpy as np

with open("input.txt") as f_hndl:
    lines = f_hndl.readlines()

copies = np.ones(len(lines))
for line_nb, line in enumerate(lines):
    winners, numbers = line[line.index(":") + 2 :].split(" | ")
    winners = set(int(i) for i in winners.split(" ") if i)
    numbers = set(int(i) for i in numbers.split(" ") if i)

    number_of_matching = len(winners.intersection(numbers))
    copies[line_nb + 1 : line_nb + number_of_matching + 1] += copies[line_nb]


print(copies.sum())
