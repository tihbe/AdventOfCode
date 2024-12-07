from operator import add, mul
from itertools import product

with open("input.txt") as f_hndl:
    output = 0
    for line in f_hndl.readlines():
        target, numbers = line.strip().split(": ")
        target = int(target)
        numbers = [int(nb) for nb in numbers.split(" ")]
        for ops in product((add, mul), repeat=len(numbers) - 1):
            total = numbers[0]
            for op, nb in zip(ops, numbers[1:]):
                total = op(total, nb)
            if total == target:
                output += total
                break
    print(output)
