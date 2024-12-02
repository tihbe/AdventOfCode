import numpy as np


def is_valid(numbers):
    # from sol1.py
    diff = np.diff(list(numbers))
    is_valid = len(np.unique(np.sign(diff))) == 1 and all(abs(diff) <= 3)
    return is_valid


count = 0
with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        numbers = list(map(float, line.split(" ")))
        if is_valid(numbers):
            count += 1
            continue

        for i in range(len(numbers)):
            one_removed = numbers[:i] + numbers[i + 1 :]
            if is_valid(one_removed):
                count += 1
                break

print(count)
