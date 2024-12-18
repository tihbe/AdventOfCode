with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        if line.startswith("Program"):
            _, program = line.split(": ")
            program = [int(i) for i in program.split(",")]


def run_program(initial_value, program):
    # from sol1.py
    registers = {
        "A": initial_value,
        "B": 0,
        "C": 0,
    }
    ptr = 0
    output = []
    iter = 0
    while ptr < len(program):
        iter += 1
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

    return output


bin2 = lambda x: format(x, "03b")  # int to bin with 3 digits


def get_possibilities(partial_solution):
    possibilities = []
    for value in range(0b1000):
        current = int(partial_solution + bin2(value), 2)
        output = run_program(current, program)
        if output == program[-len(output) :]:
            possibilities.append(value)
    return possibilities


def get_solution(partial_solution):
    current_pos = len(partial_solution) // 3
    if current_pos == len(program):  # end condition for success
        return int(partial_solution, 2)

    possibilities = get_possibilities(partial_solution)
    if len(possibilities) == 0:
        return None  # failed, no more possibilities

    for p in possibilities:
        solution = get_solution(partial_solution + bin2(p))
        if solution is not None:
            return solution

    return None


print(get_solution(""))
