with open("input.txt", "r") as f_hndl:
    cycle = 0
    register_value = 1
    width = 40
    height = 6

    screen = [["."] * width for _ in range(height)]

    def print_char():
        x = cycle % width
        y = (cycle // width) % height
        screen[y][x] = "#" if abs(x - register_value) < 2 else "."

    for line in f_hndl:
        instruction = line.rstrip().split()
        if instruction[0] == "noop":
            print_char()
            cycle += 1

        elif instruction[0] == "addx":
            print_char()
            cycle += 1

            print_char()
            cycle += 1
            register_value += int(instruction[1])

    for y in range(height):
        print("".join(screen[y]))
