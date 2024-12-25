import re
from operator import xor, or_, and_

with open("input.txt") as f_hndl:
    data = f_hndl.read()

initial_values = re.findall("([a-z]\d+): (1|0)", data)
operations = re.findall("(.+) ((?:AND)|(?:OR)|(?:XOR)) (.+) -> (.+)", data)
operators = {
    "AND": and_,
    "OR": or_,
    "XOR": xor,
}

values = {register: int(value) for register, value in initial_values}
op_processed = [False] * len(operations)
while not all(op_processed):
    for i, (operation, op_done) in enumerate(zip(operations, op_processed)):
        if op_done:
            continue
        l, op, r, out = operation
        op = operators[op]
        v1 = values.get(l, None)
        v2 = values.get(r, None)
        if v1 is None or v2 is None:
            continue
        values[out] = op(v1, v2)
        op_processed[i] = True

out = 0
for i in range(100):
    key = f"z{i:02d}"
    if key in values:
        out |= values[key] << i
    else:
        break
print(out)
