x_val = ord("X")
a_val = ord("A")
with open("input.txt", "r") as f_hndl:
    points = 0

    for line in f_hndl:
        selection = ord(line[0]) - a_val
        goal = ord(line[2]) - x_val

        if goal == 0:  # lose
            selection = (selection - 1) % 3
            points += selection + 1
        elif goal == 1:  # draw
            points += selection + 1 + 3
        else:  # win
            selection = (selection + 1) % 3
            points += selection + 1 + 6

    print(points)