import re
from tqdm import trange

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
    # solving A*btn_A + B*btn_B = prize
    # less dummy approach (¬_¬ )
    prize = (10000000000000 + prize[0], 10000000000000 + prize[1])

    # a*btn_A[0]+b*btn_B[0]=prize[0]
    # a*btn_A[1]+b*btn_B[1]=prize[1]
    # a = (prize[0]-b*btn_B[0])/btn_A[0]
    # a = (prize[1]-b*btn_B[1])/btn_A[1]
    # (prize[0]-b*btn_B[0])/btn_A[0] = (prize[1]-b*btn_B[1])/btn_A[1]
    # prize[0]/btn_A[0]-b*btn_B[0]/btn_A[0] = prize[1]/btn_A[1]-b*btn_B[1]/btn_A[1]
    # prize[0]/btn_A[0]-prize[1]/btn_A[1] = b(-btn_B[1]/btn_A[1]+btn_B[0]/btn_A[0])
    # b = (prize[0]/btn_A[0]-prize[1]/btn_A[1]) / (-btn_B[1]/btn_A[1]+btn_B[0]/btn_A[0])

    b = (prize[0] / btn_A[0] - prize[1] / btn_A[1]) / (
        -btn_B[1] / btn_A[1] + btn_B[0] / btn_A[0]
    )
    a = (prize[1] - b * btn_B[1]) / btn_A[1]
    if abs(round(a) - a) < 1e-3 and abs(round(b) - b) < 1e-3:
        total += 3 * round(a) + round(b)

print(total)
