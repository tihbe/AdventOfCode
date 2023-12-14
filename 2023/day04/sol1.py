with open("input.txt") as f_hndl:
    lines = f_hndl.readlines()

points = 0
for line in lines:
    winners, numbers = line[line.index(":") + 2 :].split(" | ")
    winners = set(int(i) for i in winners.split(" ") if i)
    numbers = set(int(i) for i in numbers.split(" ") if i)

    points += int(pow(2, len(winners.intersection(numbers)) - 1))

print(points)
