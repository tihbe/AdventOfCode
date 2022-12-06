x_val = ord("X")
delta = x_val - ord("A")
with open("input.txt", "r") as f_hndl:
    points = 0

    for line in f_hndl:
        a = ord(line[0]) - ord(line[2]) + delta
        if a == -1 or a == 2:
            points += 6
        elif a == 0:  # draw
            points += 3

        points += ord(line[2]) - x_val + 1

    print(points)