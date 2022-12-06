from string import ascii_letters

with open("input.txt", "r") as f_hndl:
    priority_sum = 0
    previous_lines = []
    for i, line in enumerate(f_hndl):
        if (i % 3) < 2:
            previous_lines.append(line)
        else:
            common_char = set(line.rstrip()).intersection(previous_lines[0]).intersection(previous_lines[1]).pop()
            priority_sum += 1 + ascii_letters.index(common_char)  # Slow lookup
            previous_lines.clear()
    print(priority_sum)
