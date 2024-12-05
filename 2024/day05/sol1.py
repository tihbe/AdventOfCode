from collections import defaultdict

rules = defaultdict(set)
total = 0
with open("input.txt") as f_hndl:
    for line in f_hndl.readlines():
        if "|" in line:
            before, after = (int(x) for x in line.split("|"))
            rules[before].add(after)
        elif "," in line:
            numbers = [int(x) for x in line.split(",")]
            seen = set()
            for number in numbers:
                if len(rules[number].intersection(seen)) > 0:
                    break
                seen.add(number)
            else:  # numbers valid
                total += numbers[len(numbers) // 2]

print(total)
