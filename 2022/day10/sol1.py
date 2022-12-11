with open("input.txt", "r") as f_hndl:
    cycle = 0
    register_value = 1
    target_cycles = set([20, 60, 100, 140, 180, 220])
    total_strength = 0

    def get_strength():
        return register_value * cycle if cycle in target_cycles else 0

    for line in f_hndl:
        instruction = line.rstrip().split()
        if instruction[0] == "noop":
            cycle += 1
            total_strength += get_strength()

        elif instruction[0] == "addx":
            cycle += 1
            total_strength += get_strength()
            cycle += 1
            total_strength += get_strength()

            register_value += int(instruction[1])

    print(total_strength)