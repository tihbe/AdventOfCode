with open("input.txt") as f:
    batteries = f.readlines()

total = 0
for battery in batteries:
    battery = battery.strip()
    numbers = [int(c) for c in battery]
    left_value = max(numbers[:-1])
    left_index = numbers.index(left_value)
    right_value = max(numbers[left_index + 1 :])

    total += 10 * left_value + right_value


print(total)
