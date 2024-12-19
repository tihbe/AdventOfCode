with open("input.txt") as f_hndl:
    designs = []
    for line in f_hndl.readlines():
        line = line.strip()
        if "," in line:
            patterns = line.split(", ")
        elif len(line) > 0:
            designs.append(line)


def is_possible(design: str):
    if len(design) == 0:
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if is_possible(design[len(pattern) :]):
                return True
    return False


count_possible = sum(is_possible(design) for design in designs)
print(count_possible)
