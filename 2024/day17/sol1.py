registers = {}
with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        if line.startswith("Register"):
            register, value = line.split(": ")
            registers[register.split(" ")[1]] = int(value)
        elif line.startswith("Program"):
            _, program = line.split(": ")
            program = [int(i) for i in program.split(",")]


ptr = 0
output = []
while ptr < len(program):
    opcode = program[ptr]
    operand = program[ptr + 1]

    if operand == 4:
        combo = registers["A"]
    elif operand == 5:
        combo = registers["B"]
    elif operand == 6:
        combo = registers["C"]
    else:
        combo = operand

    if opcode == 0:
        registers["A"] //= pow(2, combo)
    elif opcode == 1:
        registers["B"] ^= operand
    elif opcode == 2:
        registers["B"] = combo % 8
    elif opcode == 3 and registers["A"] != 0:
        ptr = operand
        continue
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:
        output.append(combo % 8)
    elif opcode == 6:
        registers["B"] = registers["A"] // pow(2, combo)
    elif opcode == 7:
        registers["C"] = registers["A"] // pow(2, combo)

    ptr += 2

print(",".join(map(str, output)))
