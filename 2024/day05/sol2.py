from collections import defaultdict

rules = defaultdict(set)
total = 0
with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        if "|" in line:
            before, after = (int(x) for x in line.split("|"))
            rules[before].add(after)
        elif "," in line:
            iterations = 0
            numbers = [int(x) for x in line.split(",")]

            while True:
                seen = set()
                numbers_to_swap = None
                for i, number in enumerate(numbers):
                    culprit = rules[number].intersection(seen)
                    if len(culprit) > 0:
                        numbers_to_swap = i, numbers.index(culprit.pop())
                        break
                    seen.add(number)
                else:  # numbers valid
                    break

                i, j = numbers_to_swap
                numbers[j], numbers[i] = numbers[i], numbers[j]
                iterations += 1

            if iterations > 0:
                total += numbers[len(numbers) // 2]

print(total)
