import numpy as np

count = 0
with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        numbers = map(float, line.split(" "))
        diff = np.diff(list(numbers))
        is_valid = len(np.unique(np.sign(diff))) == 1 and all(abs(diff) <= 3)
        count += is_valid

print(count)
