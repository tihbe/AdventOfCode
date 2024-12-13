import re

claw_machines = []
with open("input.txt") as f_hndl:
    claw_machine = []
    text = f_hndl.read()
    for match in re.findall("((?:Button [AB])|Prize): X[+=](\d+), Y[+=](\d+)", text):
        _, x, y = match
        claw_machine.append((int(x), int(y)))
        if len(claw_machine) == 3:
            claw_machines.append(claw_machine)
            claw_machine = []

total = 0
for btn_A, btn_B, prize in claw_machines:
    # solving A*btn_A + B*btn_B = prize with a loop
    solution = None
    for btn_a_press in range(100):  # start with A press as low as possible
        dx = prize[0] - btn_a_press * btn_A[0]
        dy = prize[1] - btn_a_press * btn_A[1]
        if dx < 0 or dy < 0:
            break  # impossible
        if dx % btn_B[0] == 0 and dy % btn_B[1] == 0:
            press_x = dx // btn_B[0]
            press_y = dy // btn_B[1]
            if press_x <= 100 and press_x == press_y:
                solution = (btn_a_press, press_x)
                break
    if solution is not None:
        total += 3 * solution[0] + solution[1]
print(total)
