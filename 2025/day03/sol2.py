with open("input.txt") as f:
    batteries = f.readlines()

total = 0
for battery in batteries:
    battery = battery.strip()
    numbers = [int(c) for c in battery]
    battery_voltage = 0
    values = [0] * 12

    start_index = 0
    for i in range(0, len(values)):
        remaining_numbers = numbers[start_index : len(numbers) - len(values) + i + 1]
        values[i] = max(remaining_numbers)
        start_index = remaining_numbers.index(values[i]) + start_index + 1
        battery_voltage = battery_voltage * 10 + values[i]

    total += battery_voltage


print(total)
