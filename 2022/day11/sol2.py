import re
from collections import defaultdict
from operator import add, mul, pow
import numpy as np

monkey_items = [{} for _ in range(10_000 + 1)]
monkey_operations = {}
monkey_test = defaultdict(dict)

# Parse data
with open("input.txt", "r") as f_hndl:
    current_monkey = None
    for line in f_hndl:
        if match := re.match("^Monkey (\d+):$", line):
            current_monkey = match.group(1)
        elif match := re.match("^\s\sStarting items:((?: \d+,?)+)$", line):
            monkey_items[0][current_monkey] = [int(nb) for nb in match.group(1).split(",")]
        elif match := re.match("^\s\sOperation: new = old (.+) (\d+|old)$", line):
            operator_map = {"*": mul, "+": add}
            operator = operator_map[match.group(1)]
            val = match.group(2)
            if val == "old" and operator is mul:
                operator = pow
                val = 2
            else:
                val = int(val)
            monkey_operations[current_monkey] = (operator, val)
        elif match := re.match("^\s\sTest: divisible by (\d+)$", line):
            monkey_test[current_monkey]["divisor"] = int(match.group(1))
        elif match := re.match("^\s{4}If (true|false): throw to monkey (\d+)$", line):
            monkey_test[current_monkey][match.group(1)] = match.group(2)

monkeys = sorted(monkey_items[0].keys())
lcm = np.lcm.reduce([test["divisor"] for test in monkey_test.values()])

# Process rounds
inspections = defaultdict(int)
for round in range(10_000):
    for monkey in list(monkeys):
        if monkey not in monkey_items[round]:
            continue

        items = monkey_items[round][monkey]
        inspections[monkey] += len(items)
        op = monkey_operations[monkey]
        test = monkey_test[monkey]
        for i, worry_level in enumerate(items):

            start_level = worry_level
            worry_level = op[0](worry_level, op[1]) % lcm
            next_monkey = test["true" if worry_level % test["divisor"] == 0 else "false"]
            next_round = round + 1 if next_monkey <= monkey else round
            if next_monkey not in monkey_items[next_round]:
                monkey_items[next_round][next_monkey] = []
            monkey_items[next_round][next_monkey].append(worry_level)


top_inspections = list(sorted(inspections.values()))[-2:]
print(mul(*top_inspections))
# print(monkey_items)
