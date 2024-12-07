from operator import add, mul
from itertools import product
from tqdm.auto import tqdm
import math


def concat(x: int, y: int) -> int:
    # about the same time as int(str(x)+str(y))   (ノಠ益ಠ)ノ彡┻━┻
    return pow(10, math.floor(math.log10(y)) + 1) * x + y


with open("input.txt") as f_hndl:
    output = 0

    for line in tqdm(f_hndl.readlines()):
        target, numbers = line.strip().split(": ")
        target = int(target)
        numbers = [int(nb) for nb in numbers.split(" ")]
        for ops in product((add, mul, concat), repeat=len(numbers) - 1):
            total = numbers[0]
            for op, nb in zip(ops, numbers[1:]):
                total = op(total, nb)
            if total == target:
                output += total
                break
    print(output)
