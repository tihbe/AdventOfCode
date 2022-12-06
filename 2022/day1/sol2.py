max_cal = [0] * 3

with open("input.txt", "r") as f_hndl:
    current_elf_cals = 0
    for line in f_hndl:
        if len(line) <= 1:
            max_cal[0] = max(max_cal[0], current_elf_cals)
            max_cal.sort()
            current_elf_cals = 0
        else:
            current_elf_cals += int(line)

print(sum(max_cal))