import re
from collections import defaultdict

with open("input.txt", "r") as f_hndl:
    stacks = defaultdict(list)

    currently_processing_stacks = True
    stack_regex = re.compile("(\s{3}|\[.\])\s")
    for line in f_hndl:
        if len(line) == 1 and len(stacks) > 0:
            currently_processing_stacks = False
            continue

        if currently_processing_stacks:
            elements = re.findall(stack_regex, line)

            for i, element in enumerate(elements):
                element = element.rstrip()
                if len(element) > 0:
                    stacks[i].append(element)
        else:
            elements = line.split(" ")
            _, nb_elements, _, start_pos, _, end_pos = elements
            nb_elements = int(nb_elements)
            start_pos = int(start_pos) - 1
            end_pos = int(end_pos) - 1

            for n in range(nb_elements):
                container = stacks[start_pos].pop(0)
                stacks[end_pos].insert(0, container)

    message = "".join(stacks[i][0][1] for i in range(len(stacks)))  # top container at index 0, 2nd char for id
    print(message)