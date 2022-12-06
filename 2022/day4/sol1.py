import re

with open("input.txt", "r") as f_hndl:
    seat_pos_regex = re.compile(",|-")
    overlaps = 0
    for line in f_hndl:
        l0, r0, l1, r1 = seat_pos_regex.split(line)
        l0, r0, l1, r1 = int(l0), int(r0), int(l1), int(r1)
        if l0 >= l1 and r0 <= r1:
            overlaps += 1
        elif l1 >= l0 and r1 <= r0:
            overlaps += 1

    print(overlaps)