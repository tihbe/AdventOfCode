from string import ascii_letters

with open("input.txt", "r") as f_hndl:
    priority_sum = 0
    for line in f_hndl:
        half_len = len(line) // 2
        left, right = line[:half_len], line[half_len:]
        common_char = set(left).intersection(right).pop()
        priority_sum += 1 + ascii_letters.index(common_char)  # Slow lookup
    print(priority_sum)
