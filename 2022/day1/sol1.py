max_cal = 0
with open("input.txt", "r") as f_hndl:
    current_elf_cals = 0
    for line in f_hndl:
        if len(line) <= 1:
            max_cal = max(max_cal, current_elf_cals)
            current_elf_cals = 0
        else:
            current_elf_cals += int(line)

print(max_cal)