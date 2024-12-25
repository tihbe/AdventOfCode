import re
from operator import xor, or_, and_

with open("input.txt") as f_hndl:
    data = f_hndl.read()

operations = re.findall("(.+) ((?:AND)|(?:OR)|(?:XOR)) (.+) -> (.+)", data)
operators = {
    "AND": and_,
    "OR": or_,
    "XOR": xor,
}

# Answer here, done iteratively
swaps = [
    ["z10", "gpr"],
    ["z21", "nks"],
    ["z33", "ghp"],
    ["krs", "cpm"],
]
for i in range(len(operations)):
    operation = operations[i]
    for swap in swaps:
        if operation[3] == swap[0]:
            operations[i] = [*operation[:3], swap[1]]
            break
        elif operation[3] == swap[1]:
            operations[i] = [*operation[:3], swap[0]]
            break


class Node:
    left = None
    right = None
    op = None

    def __init__(self, wire: str):
        self.wire = wire

    def __repr__(self):
        if self.op is not None:
            return f"({self.left} {self.op} {self.right})"
        else:
            return self.wire

    def __call__(self, values):
        if self.wire in values:
            return values[self.wire]
        return operators[self.op](self.left(values), self.right(values))


tree = {}
for l, op, r, out in operations:
    if l not in tree:
        tree[l] = Node(l)
    if r not in tree:
        tree[r] = Node(r)
    if out not in tree:
        tree[out] = Node(out)

    tree[out].left = tree[l]
    tree[out].right = tree[r]
    tree[out].op = op

# for each bit, test addition with no carry
# if it fails, error is there
# for now I check the equation and the error is easy to notice
# I then update above swap list to fix the error
values = {}
for i in range(44):
    key = f"z{i:02d}"
    x = f"x{i:02d}"
    y = f"y{i:02d}"
    values[x] = values[y] = 0
    print(key, "=", tree[key])
    if i > 0:
        for a in range(2):
            for b in range(2):
                out = tree[key]({**values, x: a, y: b})
                assert out == (a ^ b), f"Error at {key}"

print(",".join(sorted(sum(swaps, []))))  # all done w/o testing for bit carry logic :)
