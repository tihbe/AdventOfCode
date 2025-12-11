from z3 import Int, Optimize, Sum, sat

with open("input.txt") as f_hndl:
    lines = f_hndl.readlines()


total = 0
for line in lines:
    parts = line.strip().split(" ")
    buttons = [set(map(int, button.strip("()").split(","))) for button in parts[1:-1]]
    target_joltage = tuple(map(int, parts[-1].strip("{}").split(",")))

    num_buttons = len(buttons)
    num_coords = len(target_joltage)

    s_button_presses = [Int(btn) for btn in range(len(buttons))]
    opt = Optimize()

    for v in s_button_presses:
        opt.add(v >= 0)

    for coord in range(num_coords):
        opt.add(
            Sum(
                [
                    s_button_presses[btn]
                    for btn in range(num_buttons)
                    if coord in buttons[btn]
                ]
            )
            == int(target_joltage[coord])
        )

    opt.minimize(Sum(s_button_presses))
    assert opt.check() == sat
    model = opt.model()
    presses = [model[v].as_long() for v in s_button_presses]
    total += sum(presses)

print(total)
