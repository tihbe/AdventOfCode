from math import log10, floor
from collections import defaultdict


def blink(number):
    if number == 0:
        return (1,)
    elif (digits := floor(log10(number))) % 2 == 1:
        exp = int(pow(10, (digits + 1) // 2))
        left = number // exp
        right = number % exp
        return (left, right)
    else:
        return (number * 2024,)


with open("input.txt") as f_hndl:
    numbers = [int(n) for n in f_hndl.readline().strip().split(" ")]

numbers = {nb: 1 for nb in numbers}  # number, appearance count
for _ in range(25):
    idx = 0
    next_numbers = defaultdict(int)
    for number, count in numbers.items():
        for nb in blink(number):
            next_numbers[nb] += count
    numbers = next_numbers

print(sum(numbers.values()))
